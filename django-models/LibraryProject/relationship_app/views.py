from .models import Library
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile
# Function-based view to list all books


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view to show library details

class LibraryDetailView(DetailView):
    model = Library  # Reference the Library model
    # Template for displaying the library details
    template_name = 'relationship_app/library_detail.html'
    # Use 'library' as the context variable name in the template
    context_object_name = 'library'


# Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            # Authenticate the user
            user = authenticate(username=username, password=password)
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to home or any other page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# These views are built-in


class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'


# Helper function to check roles
def user_is_admin(user):
    return user.userprofile.role == 'Admin'


def user_is_librarian(user):
    return user.userprofile.role == 'Librarian'


def user_is_member(user):
    return user.userprofile.role == 'Member'

# Admin View


@login_required
@user_passes_test(user_is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian View


@login_required
@user_passes_test(user_is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member View


@login_required
@user_passes_test(user_is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
