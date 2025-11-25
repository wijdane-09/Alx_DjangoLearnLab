from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# -------------------------
# LIST VIEW
# -------------------------
class ListView(generics.ListAPIView):
    """
    Retrieve all books (read-only).
    Accessible to all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# -------------------------
# DETAIL VIEW
# -------------------------
class DetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by ID.
    Accessible to all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# -------------------------
# CREATE VIEW
# -------------------------
class CreateView(generics.CreateAPIView):
    """
    Create a new book.
    Only authenticated users can create.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# -------------------------
# UPDATE VIEW
# -------------------------
class UpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    Only authenticated users can update.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# -------------------------
# DELETE VIEW
# -------------------------
class DeleteView(generics.DestroyAPIView):
    """
    Delete an existing book.
    Only authenticated users can delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
