from django.contrib import admin

from library.models import Author, Book, Borrowing


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date', 'book_count']
    search_fields = ['name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'available_copies']
    search_fields = ['title', 'author']

@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ['book', 'reader', 'borrowed_date', 'is_returned']
    search_fields = ['book', 'reader']

