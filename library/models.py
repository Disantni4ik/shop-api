import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Reader(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(max_length=100, blank=True)
    registration_date = models.DateField(auto_now_add=True)

class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=500)
    birth_date = models.DateField(blank=True)
    photo = models.ImageField(upload_to='authors/', blank=True)

    def __str__(self):
        return self.name

    @property
    def book_count(self):
        pass

class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    pages = models.PositiveIntegerField()
    cover = models.ImageField(upload_to='books/', blank=True)
    available_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    @property
    def is_available(self):
        if self.available_copies > 0:
            return True
        else:
            return False

class Borrowing(models.Model):
    book = models.ForeignKey(Book, related_name='borrowings', on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, related_name='borrowings', on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return (f"Book: {self.book.title}\n"
                f"Borrowed date: {self.borrowed_date}\n"
                f"Return date: {self.return_date}\n"
                f"Returned: {self.is_returned}")

    @property
    def days_borrowed(self):
        return (timezone.now() - self.borrowed_date).day


