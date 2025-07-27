from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Book


@permission_required('yourapp.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'yourapp/book_list.html', {'books': books})


@permission_required('yourapp.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Handle form submission to create book
        pass
    return render(request, 'yourapp/create_book.html')


@permission_required('yourapp.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Handle editing logic here
        pass
    return render(request, 'yourapp/edit_book.html', {'book': book})


@permission_required('yourapp.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'yourapp/confirm_delete.html', {'book': book})
