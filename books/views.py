from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from books.forms import BookCreateForm, BookUpdateForm
from books.models import Book


# Create your views here.


class BooksListView(ListView):
    template_name = 'books/books_list.html'
    model = Book
    context_object_name = 'books'

    def get_context_data(self,*args,  **kwargs):
        context = super().get_context_data(*args, **kwargs)
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page = self.request.GET.get('page')
        try:
            books = paginator.page(page)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)

        context['books'] = books
        return context


class BookCreateView(CreateView):
    template_name = 'books/book_form.html'
    model = Book
    form_class = BookCreateForm
    success_url = reverse_lazy('books_list')

    def test_func(self):
        return self.request.user.is_superuser


# Update Book view
class BookUpdateView(UpdateView):
    model = Book
    form_class = BookUpdateForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('books_list')

    def test_func(self):
        return self.request.user.is_superuser


# Delete Book view
class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
    template_name = 'books/book_confirm_delete.html'

    def test_func(self):
        return self.request.user.is_superuser


# Book Detail view
class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
