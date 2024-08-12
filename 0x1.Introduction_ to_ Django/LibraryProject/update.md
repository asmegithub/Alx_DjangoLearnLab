# command used

>>> from bookshelf.models import Book
>>> Book.objects.filter(title='1984').update(title="Nineteen Eighty-Four")

# output: 1 (i item successfully updated!)

