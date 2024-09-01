from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from .forms import CustomBookForm

# Create your views here.


def index(request):
    return HttpResponse("Hey this book shelf page!")


def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})


def view_book(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'bookshelf/view_book.html', {'book': book})


@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = CustomBookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomBookForm()
    return render(request, 'bookshelf/create_book.html', {'form': form})


@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = CustomBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
    else:
        form = CustomBookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form})


@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'bookshelf/delete_book.html', {'book': book})
