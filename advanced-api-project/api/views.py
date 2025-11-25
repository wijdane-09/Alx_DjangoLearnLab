from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# --------------------------
# LIST + CREATE VIEW
# --------------------------
class BookListCreateView(generics.ListCreateAPIView):
    """
    View for listing all books and creating new ones.
    - GET: accessible to everyone (read-only)
    - POST: only authenticated users can create books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions:
    # Allow unsafe methods (POST) only for authenticated users
    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


# --------------------------
# RETRIEVE + UPDATE + DELETE VIEW
# --------------------------
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a single book.
    - GET: accessible to everyone
    - PUT/PATCH/DELETE: only authenticated users
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions for update & delete
    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
