# command used

>>> from bookshelf.models import Book
>>> book=Book.objects.filter(title='1984')
>>> book.title="Nineteen Eighty-Four"
>>> book.save()

# output: 1 (i item successfully updated!)

