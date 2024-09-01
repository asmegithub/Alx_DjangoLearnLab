from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, view_book, create_book, edit_book, delete_book

from . import views
urlpatterns = [
    path('', list_books, name='list_books'),
    path('create_book/', create_book, name='create_book'),
    path('view_book/<int:book_id>', view_book, name='view_book'),
    path('edit_book/<int:book_id>', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>', delete_book, name='delete_book'),
    # path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='bookshelf/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
