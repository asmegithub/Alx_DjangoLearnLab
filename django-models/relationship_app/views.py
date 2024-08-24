from django.shortcuts import render
from django.views.generic.detail import DetailView


from models import Book
from .models import Library


def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, './templates/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = './templates/library_detail.html'
    context_object_name = 'library'
