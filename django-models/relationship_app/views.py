from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Book, Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView


def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_applist_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = './templates/'
    context_object_name = 'library'


class LoginView(LoginView):
    template_name = './templates/users/login.html'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, './templates/users/register.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'templates/users/register.html', {'form': form})
