from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from library.filters import BookFilter, BorrowingFilter, AvailableBooksFilterBackend, ActiveBorrowingsFilterBackend
from library.models import Author, Book, Borrowing
from library.serializers import (
    AuthorSerializer,
    BookSerializer,
    BookDetailSerializer,
    BorrowingSerializer,
)


class AuthorListAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_url_kwarg = 'author_id'

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.select_related('author')
    serializer_class = BookSerializer
    filterset_class = BookFilter

class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BorrowingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Borrowing.objects.prefetch_related('book', 'reader')
    serializer_class = BorrowingSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = BorrowingFilter

class AvailableBookListAPIView(generics.ListAPIView):
    queryset = Book.objects.filter(available_copies__gt=0)
    serializer_class = BookSerializer

class AvailableBooksAPIView(generics.ListAPIView):
    queryset = Book.objects.select_related('author').order_by('pk')
    serializer_class = BookSerializer
    filter_backends = [
        DjangoFilterBackend,
        AvailableBooksFilterBackend,
    ]
    filterset_class = BookFilter

class ActiveBorrowingsAPIView(generics.ListAPIView):
    queryset = Borrowing.objects.prefetch_related('book', 'reader').order_by('-borrowed_date')
    serializer_class = BorrowingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        ActiveBorrowingsFilterBackend,
    ]
    filterset_class = BorrowingFilter