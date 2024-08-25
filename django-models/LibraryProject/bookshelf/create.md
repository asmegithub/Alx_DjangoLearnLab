# create.md
# command to create book instance

>>> from bookshelf.models import Book
>>> b=Book.objects.create(title='1984',author='George Orwell',publication_year=1949)

# Output: the new Book instance is successfully created!!
