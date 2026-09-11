from django.urls import path

from library import views

app_name = 'library'

urlpatterns = [
    path('authors/', views.AuthorListAPIView.as_view(), name='author_list'),
    path('authors/<int:author_id>/', views.AuthorDetailAPIView.as_view(), name='author_detail'),
    path('books/', views.BookListCreateAPIView.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetailAPIView.as_view(), name='book_detail'),
    path('borrowings/', views.BorrowingListCreateAPIView.as_view(), name='borrowing_list'),
    path('books/available/', views.AvailableBookListAPIView.as_view(), name='available_books'),
]