from django.urls import path
from .views import list_books, LibraryDetailView  # ✅ تأكد من وجود list_books هنا

urlpatterns = [
    path('books/', list_books, name='list_books'),  # ✅ لعرض جميع الكتب
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # ✅ لعرض مكتبة واحدة
]