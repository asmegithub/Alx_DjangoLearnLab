from relationship_app.models import Book, Author, Library

# Query all books by a specific author
author = Author.objects.get(name="John Doe")
books_by_author = Book.objects.filter(author=author)
print(books_by_author)

# List all books in a library
library_name = 'Main Library'
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()  # Add this line
print(books_in_library)

# Retrieve the librarian for a library
library = Library.objects.get(name="Main Library")
librarian = library.librarian
print(librarian)
