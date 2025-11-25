from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer


# -------------------------
# LIST VIEW
# -------------------------
class ListView(generics.ListAPIView):
    """
    Retrieve all books (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# -------------------------
# DETAIL VIEW
# -------------------------
class DetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# -------------------------
# CREATE VIEW
# -------------------------
class CreateView(generics.CreateAPIView):
    """
    Create a new book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# -------------------------
# UPDATE VIEW
# -------------------------
class UpdateView(generics.UpdateAPIView):
    """
    Update a book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# -------------------------
# DELETE VIEW
# -------------------------
class DeleteView(generics.DestroyAPIView):
    """
    Delete a book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
