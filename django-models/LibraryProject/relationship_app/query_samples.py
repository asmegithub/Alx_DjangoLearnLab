from relationship_app.models import Book, Author, Library, Librarian

# Query all books by a specific author
author_name = 'John Doe'
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(books_by_author)

# List all books in a library
library_name = 'Main Library'
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(books_in_library)

# Retrieve the librarian for a library
library_name = 'Main Library'
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
print(librarian)
