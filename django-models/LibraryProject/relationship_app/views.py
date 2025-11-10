from django.shortcuts import render ,redirect
from django.contrib.auth import login  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib import messages
from django.views.generic.detail import DetailView
from .models import Book, Library  
from .models import Library

# ------------------------------
# Function-based view
# ------------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# ------------------------------
# Class-based view
# ------------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  
    context_object_name = 'library'  

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm()  
        form = UserCreationForm(request.POST)  
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()  
    return render(request, 'relationship_app/register.html', {'form': form})