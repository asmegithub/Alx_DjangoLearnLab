
# Command to retrive data:
>>> from bookshelf.models import Book
>>> b=Book.objects.get(title='1984')
>>> print(b)

# output: 
<QuerySet [<Book: title= 1984 author= George Orwell publication year= 1949>]>

# the above output can be acheved by __str__ method defined inside the Book class in models.py file
