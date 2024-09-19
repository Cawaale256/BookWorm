from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Member
from .forms import BookForm, MemberForm, BorrowForm, ReturnForm, ExtendForm

# Home view
def home(request):
    # Render the home page
        return render(request, 'library/home.html')

# Book list view
def book_list(request):
        # Retrieve all books from the database
        books = Book.objects.all()
        # Render the book list page with the retrieved books
        return render(request, 'library/book_list.html', {'books': books})




