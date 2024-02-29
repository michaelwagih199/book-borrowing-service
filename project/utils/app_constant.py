from enum import Enum


class AppResourcesUri(Enum):
    BOOKS_LIST_VIEW = "books"
    BOOKS_DETAILS_VIEW = "books/<int:book_id>"
    BOOKS_SHOW_AVAILABLE = "books/available"
    BORROWING_BOOK = "books/borrowing"

class BOOK_STATUES(Enum):
    AVAILABLE = "AVAILABLE"
    FREEZE = "FREEZE"
    BORROWED = "BORROWED"


class AppErrorMessages:
    OK = "Success"
    NOT_Found = "NotFound"
    DELETED = "Deleted Successfully"
    BOOK_AVAILABLE = "Book Available To Borrow"
    BOOK_NOT_AVAILABLE = "Book Not Available To Borrow"
    INVALID_DATES = "Invalid Date"
