from datetime import date

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from library.models import Book, Borrowing, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'birth_date', 'photo']

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'isbn', 'published_date', 'pages', 'cover', 'available_copies', 'is_available']

        def validate_pages(self, pages):
            if pages > 0:
                return pages

        def validate_isbn(self, isbn):
            if len(isbn) == 13:
                return isbn

class BorrowingSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)
    reader_name = serializers.CharField(source='reader.username', read_only=True)
    days_borrowed = serializers.SerializerMethodField()

    class Meta:
        model = Borrowing
        fields = [
            'id', 'book_title', 'reader_name',
            'borrowed_date', 'return_date', 'is_returned',
            'days_borrowed'
        ]

    def get_days_borrowed(self, obj):
        if not obj.borrowed_date:
            return 0

        if obj.is_returned and obj.return_date:
            end_date = obj.return_date
        else:
            end_date = date.today()

        return (end_date - obj.borrowed_date).days


class BookDetailSerializer(BookSerializer):
    author = AuthorSerializer(read_only=True)
    total_borrowings = serializers.SerializerMethodField()

    class Meta(BookSerializer.Meta):
        fields = BookSerializer.Meta.fields + ['total_borrowings']

    def get_total_borrowings(self, obj):
        return obj.borrowings.count()