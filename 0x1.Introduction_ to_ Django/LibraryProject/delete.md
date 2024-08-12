# command used
>>> from bookshelf.models import Book
>>> Book.objects.filter(title='Nineteen Eighty-Four').delete()

# output confirming the deletion
(1, {'bookshelf.Book': 1})
