from django.shortcuts import render
from rest_framework import generics
# generics.ListAPIview=>  this has only GET method

# this has both GET and POST method
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets


from .serializers import BookSerializer
from .models import Book


# class BookList(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
