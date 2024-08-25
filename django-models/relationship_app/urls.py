from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import list_books
from .views import LibraryDetailView
from .views import LoginView
from .views import register
from . import views

urlpatterns = [
    path('', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(),
         name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
