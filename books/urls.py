from django.urls import path

from books.views import BooksListView, BookCreateView, BookUpdateView, BookDeleteView, BookDetailView

urlpatterns = [
    path('books_list/', BooksListView.as_view(), name='books_list'),
    path('books_create/<int:pk>', BookCreateView.as_view(), name='book_create'),
    path('book_update/<int:pk>', BookUpdateView.as_view(), name='book_update'),
    path('book_delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
    path('book_detail/<int:pk>', BookDetailView.as_view(), name='book_detail'),

]