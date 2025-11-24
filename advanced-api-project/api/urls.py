from django.urls import path
from .views import (
    BookListView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),        # ListView
    path('books/create/', BookCreateView.as_view(), name='book-create'), # CreateView
    path('books/<int:pk>/', BookUpdateView.as_view(), name='book-update'), # UpdateView
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'), # DeleteView
]
