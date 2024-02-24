from django.urls import path

from project.utils import app_constant

from .views import BookDetailsApiView, BookListApiView, getAvailableBooks, borrowingBook

urlpatterns = [
    path(app_constant.AppResourcesUri.BOOKS_LIST_VIEW.value, BookListApiView.as_view()),
    path(
        app_constant.AppResourcesUri.BOOKS_DETAILS_VIEW.value,
        BookDetailsApiView.as_view(),
    ),
    path(app_constant.AppResourcesUri.BOOKS_SHOW_AVAILABLE.value, getAvailableBooks),
    path(app_constant.AppResourcesUri.BORROWING_BOOK.value, borrowingBook),
]
