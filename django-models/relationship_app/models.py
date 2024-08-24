from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)


class Librariyan(models.Model):
    name = models.CharField(max_length=200)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
