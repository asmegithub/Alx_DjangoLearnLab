# Detailed CRUD Operations and Documentation

# create.md
# command to create book instance

>>> from bookshelf.models import Book
>>> b=Book.objects.create(title='1984',author='George Orwell',publication_year=1949)

# Output: the new Book instance is successfully created!!


# retrive.md

# Command to retrive data:
>>> from bookshelf.models import Book
>>> b=Book.objects.filter(title='1984')
>>> print(b)

# output: 
<QuerySet [<Book: title= 1984 author= George Orwell publication year= 1949>]>

# the above output can be acheved by __str__ method defined inside the Book class in models.py file


# update.md
>>> from bookshelf.models import Book
>>> Book.objects.filter(title='1984').update(title="Nineteen Eighty-Four")

# output: 1 (i item successfully updated!)


# delete.md
# command used
>>> from bookshelf.models import Book
>>> Book.objects.filter(title='Nineteen Eighty-Four').delete()

# output confirming the deletion
(1, {'bookshelf.Book': 1})


