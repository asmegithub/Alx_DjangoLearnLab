# command used
>>> from bookshelf.models import Book
>>> book=Book.objects.filter(title='Nineteen Eighty-Four')
>>> book.delete()

# output confirming the deletion
(1, {'bookshelf.Book': 1})
