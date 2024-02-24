from django.db import models
from project.utils.app_constant import BOOK_STATUES
from django.contrib.auth.models import User

class Book(models.Model):
    name = models.CharField(max_length=180, blank=False)
    description = models.TextField(max_length=200, blank=True)
    author = models.CharField(max_length=150, blank=False)
    printingVersion = models.CharField(max_length=150, blank=False)
    isAvailable = models.BooleanField(default=True)
    status = models.CharField(max_length=30,default=BOOK_STATUES.AVAILABLE.value)
    createdAt = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, blank=True)




class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    book = models.ForeignKey(Book, related_name="borrowing", on_delete=models.CASCADE)
    borrowDurationFrom = models.DateField(blank=True)
    borrowDurationTo = models.DateField(blank=True)
