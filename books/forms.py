from django import forms

from books.models import Book


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'num_page',  'author', 'description', 'file']


class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'num_page',  'author', 'description', 'file']