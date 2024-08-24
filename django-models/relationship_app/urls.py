from django.urls import path
from . import views
from .views import LibraryDetailView

urlpatterns = [
    path('libraries/', views.list_libraries, name='list_libraries'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
