from django.urls import path
from .views import LibraryDetailView
from . import views
from django.urls import path
from .views import LibraryDetailView, list_books
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    # Add your new paths here
    path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]
