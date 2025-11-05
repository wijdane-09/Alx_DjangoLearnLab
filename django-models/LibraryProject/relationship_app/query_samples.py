import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from LibraryProject.relationship_app.models import Author, Book, Library, Librarian


author1 = Author.objects.create(name="J.K. Rowling")
author2 = Author.objects.create(name="George R.R. Martin")

book1 = Book.objects.create(title="Harry Potter", author=author1)
book2 = Book.objects.create(title="Harry Potter 2", author=author1)
book3 = Book.objects.create(title="Game of Thrones", author=author2)

library = Library.objects.create(name="Central Library")
library.books.set([book1, book3])

librarian = Librarian.objects.create(name="Alice", library=library)




jk_books = Book.objects.filter(author__name="J.K. Rowling")
print("Books by J.K. Rowling:", [book.title for book in jk_books])


library_name = "Central Library"
library = Library.objects.get(name=library_name)
library_books = library.books.all()
print(f"Books in {library_name}:", [book.title for book in library_books])


library_librarian = Librarian.objects.get(library=library)
print("Librarian of Central Library:", library_librarian.name)
