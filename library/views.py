from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Member  # Import Book and Member models

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

# Book detail view
def book_detail(request, id):
    # Retrieve a specific book by its ID or return a 404 error if not found
    book = get_object_or_404(Book, id=id)
    # Render the book detail page with the retrieved book
    return render(request, 'library/book_detail.html', {'book': book})

# Member list view
def member_list(request):
    # Retrieve all members from the database
    members = Member.objects.all()
    # Render the member list page with the retrieved members
    return render(request, 'library/member_list.html', {'members': members})

# Member detail view
def member_detail(request, id):
    # Retrieve a specific member by their ID or return a 404 error if not found
    member = get_object_or_404(Member, id=id)
    # Render the member detail page with the retrieved member
    return render(request, 'library/member_detail.html', {'member': member})





