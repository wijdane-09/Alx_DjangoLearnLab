# CRUD Operations on Book Model

## Create
```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book
# <Book: 1984 by George Orwell (1949)>
# The book was created successfully.


from bookshelf.models import Book

books = Book.objects.all()
for b in books:
    print(b.title, b.author, b.publication_year)
# 1984 George Orwell 1949
# Retrieved book details successfully.


book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
# <Book: Nineteen Eighty-Four by George Orwell (1949)>
# Updated the book title successfully.


book.delete()
Book.objects.all()
# (1, {'bookshelf.Book': 1})
# <QuerySet []>
# The book was deleted successfully.
