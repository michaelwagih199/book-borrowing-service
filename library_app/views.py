from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from project.utils.app_utils import AppErrorMessages, AppUtils
from .models import Book, Borrow
from .serializers import BookSerializer, BorrowSerializer
from rest_framework.decorators import api_view
from project.utils.app_constant import BOOK_STATUES
import datetime


class BookListApiView(APIView):
    def get(self, request):
        bookList = Book.objects.all()
        serializer = BookSerializer(bookList, many=True)
        return Response(
            AppUtils.formatAppResponse(data=serializer.data), status=status.HTTP_200_OK
        )

    def post(self, request):
        data = {
            "name": request.data.get("name"),
            "description": request.data.get("description"),
            "author": request.data.get("author"),
            "printingVersion": request.data.get("printingVersion"),
        }
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                AppUtils.formatAppResponse(data=serializer.data),
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailsApiView(APIView):

    def getBook(self, bookId):
        try:
            return Book.objects.get(id=bookId)
        except Book.DoesNotExist:
            return None

    def get(self, request, book_id):
        book = self.getBook(book_id)
        if not book:
            return Response(
                AppUtils.formatAppResponse(
                    AppErrorMessages.NOT_Found, f"book Not {book_id} found", ""
                ),
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = BookSerializer(book)
        return Response(
            AppUtils.formatAppResponse(data=serializer.data),
            status=status.HTTP_200_OK,
        )

    def put(self, request, book_id):
        bookInstance = self.getBook(book_id)
        if not bookInstance:
            return Response(
                AppUtils.formatAppResponse(
                    AppErrorMessages.NOT_Found, f"book Not {book_id} found", ""
                ),
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = {
            "name": request.data.get("name"),
            "description": request.data.get("description"),
            "author": request.data.get("author"),
            "printingVersion": request.data.get("printingVersion"),
        }
        serializer = BookSerializer(instance=bookInstance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, book_id, *args, **kwargs):
        bookInstance = self.getBook(book_id)
        if not bookInstance:
            return Response(
                AppUtils.formatAppResponse(
                    AppErrorMessages.NOT_Found, f"book Not {book_id} found", ""
                ),
                status=status.HTTP_400_BAD_REQUEST,
            )
        bookInstance.delete()
        return Response(
            AppUtils.formatAppResponse(code=AppErrorMessages.DELETED),
            status=status.HTTP_200_OK,
        )


@api_view(["GET"])
def getAvailableBooks(request):
    borrowDate = request.query_params.get("borrowDate")
    bookId = request.query_params.get("bookId")
    
    formatDate = datetime.datetime.strptime(
        borrowDate, "%Y-%m-%d"
    )
    if isBookAvailable(bookId, formatDate):
        return Response(
            AppUtils.formatAppResponse(message=f"Be Available on Date: {borrowDate}"),
            status=status.HTTP_200_OK,
        )
    return Response(
        AppUtils.formatAppResponse(code=AppErrorMessages.BOOK_NOT_AVAILABLE),
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["POST"])
def borrowingBook(request, *args, **kwargs):
    # save borrow record and update book status
    print(request.user)
    bookId = request.data.get("bookId")
    user = request.user

    durationFrom = datetime.datetime.strptime(
        request.data.get("durationFrom"), "%Y-%m-%d"
    )

    durationTo = datetime.datetime.strptime(request.data.get("durationTo"), "%Y-%m-%d")

    today = datetime.datetime.today()

    if durationFrom < today or durationFrom > durationTo:
        return Response(
            AppUtils.formatAppResponse(
                code=AppErrorMessages.INVALID_DATES,
                message=AppErrorMessages.INVALID_DATES,
            ),
            status=status.HTTP_400_BAD_REQUEST,
        )

    bookInstance = Book.objects.get(id=bookId)
    if not bookInstance:
        return Response(
            AppUtils.formatAppResponse(
                AppErrorMessages.NOT_Found, f"book Not {bookId} found", ""
            ),
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not isBookAvailable(bookId=bookId, borrowDate=durationFrom):
        return Response(
            AppUtils.formatAppResponse(code=AppErrorMessages.BOOK_NOT_AVAILABLE),
            status=status.HTTP_400_BAD_REQUEST,
        )

    borrowInstance = Borrow()
    borrowInstance.user = user
    borrowInstance.book = bookInstance
    borrowInstance.borrowDurationFrom = durationFrom
    borrowInstance.borrowDurationTo = durationTo
    # save
    borrowInstance.save()

    # update book status
    bookInstance.status = BOOK_STATUES.BORROWED.value
    bookInstance.save()

    return Response(
        AppUtils.formatAppResponse(),
        status=status.HTTP_201_CREATED,
    )


def isBookAvailable(bookId, borrowDate):
    today = datetime.datetime.today()

    if borrowDate < today:
        return False

    isBookBeAvailableInDate = Borrow.objects.filter(
        book__pk=bookId, book__isAvailable=True, borrowDurationTo__lt=borrowDate
    )
    isBookAvailable = Book.objects.filter(
        id=bookId, status=BOOK_STATUES.AVAILABLE.value
    )
    if isBookBeAvailableInDate or isBookAvailable:
        return True
    return False
