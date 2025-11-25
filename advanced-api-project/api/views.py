from django_filters import rest_framework
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer


# -------------------------
# LIST VIEW
# -------------------------
class ListView(generics.ListAPIView):
    """
    Retrieve all books (read-only) with:
    - filtering (title, author, publication_year)
    - search (title, author name)
    - ordering (title, publication_year)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # ADD FILTERS
    filter_backends = [
        DjangoFilterBackend,   # Filtering
        SearchFilter,          # Searching
        OrderingFilter,        # Ordering
    ]

    # Filtering fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Search fields
    # author => will search inside related object's name
    search_fields = ['title', 'author__name']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']

    # Default ordering (optional)
    ordering = ['title']



# -------------------------
# DETAIL VIEW
# -------------------------
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# -------------------------
# CREATE VIEW
# -------------------------
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# -------------------------
# UPDATE VIEW
# -------------------------
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# -------------------------
# DELETE VIEW
# -------------------------
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
