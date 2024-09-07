from django.shortcuts import render
from rest_framework.generics import ListAPIView  # this has only GET method
# this has both GET and POST method
from rest_framework.generics import ListCreateAPIView

from .serializers import BookSerializer
from .models import Book


class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
