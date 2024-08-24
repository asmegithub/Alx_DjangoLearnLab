from django.shortcuts import render
from models import Author, Book, Library, Librarian
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, Book, Library, Librarian


def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
