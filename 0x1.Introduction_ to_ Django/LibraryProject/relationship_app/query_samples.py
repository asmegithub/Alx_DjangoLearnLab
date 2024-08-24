from relationship_app.models import Book, Author, Library

# Query all books by a specific author
author = Author.objects.get(name="John Doe")
books_by_author = Book.objects.filter(author=author)
print(books_by_author)

# List all books in a library
library = Library.objects.get(name="Main Library")
books_in_library = Book.objects.filter(library=library)
print(books_in_library)

# Retrieve the librarian for a library
library = Library.objects.get(name="Main Library")
librarian = library.librarian
print(librarian)
