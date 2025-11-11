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



from django.contrib.auth.decorators import user_passes_test, login_required

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


@user_passes_test(is_admin)
@login_required
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
@login_required
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
@login_required
def member_view(request):
    return render(request, 'member_view.html')
