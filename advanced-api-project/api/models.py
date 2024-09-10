from django.db import models


class Author(models.Model):
    """
    Author model represents an author entity with the following fields:

    Attributes:
        name (CharField): The name of the author. This is a character field with a maximum length of 100 characters.
    """
    name = models.CharField(max_length=100)


class Book(models.Model):
    """
    Represents a book with a title, publication year, and an associated author.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, related_name="books")
