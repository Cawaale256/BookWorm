from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm


def home(request):
    return render(request, 'library/home.html')

# View to list all books
def book_list(request):
    # Retrieve all book instances from the database
    books = Book.objects.all()
    # Render the 'book_list.html' template with the list of books
    return render(request, 'library/book_list.html', {'books': books})

# View to create a new book
@login_required  # Ensure the user is logged in to access this view
def book_create(request):
    if request.method == 'POST':
        # Create a form instance with the submitted data
        form = BookForm(request.POST)
        if form.is_valid():
            # Save the new book instance to the database
            form.save()
            # Redirect to the book list view
            return redirect('book_list')
    else:
        # Create an empty form instance
        form = BookForm()
    # Render the 'book_form.html' template with the form
    return render(request, 'library/book_form.html', {'form': form})

# View to update an existing book
@login_required  # Ensure the user is logged in to access this view
def book_update(request, pk):
    # Retrieve the book instance by primary key (pk) or return a 404 error if not found
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Create a form instance with the submitted data and the existing book instance
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            # Save the updated book instance to the database
            form.save()
            # Redirect to the book list view
            return redirect('book_list')
    else:
        # Create a form instance with the existing book instance
        form = BookForm(instance=book)
    # Render the 'book_form.html' template with the form
    return render(request, 'library/book_form.html', {'form': form})

# View to delete a book
@login_required  # Ensure the user is logged in to access this view
def book_delete(request, pk):
    # Retrieve the book instance by primary key (pk) or return a 404 error if not found
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Delete the book instance from the database
        book.delete()
        # Redirect to the book list view
        return redirect('book_list')
    # Render the 'book_confirm_delete.html' template with the book instance
    return render(request, 'library/book_confirm_delete.html', {'book': book})

# User dashboard view
@login_required  # Ensure the user is logged in to access this view
def user_dashboard(request):
    # Retrieve all books borrowed by the logged-in user
    borrowed_books = Book.objects.filter(borrower=request.user)
    # Render the 'user_dashboard.html' template with the list of borrowed books
    return render(request, 'library/user_dashboard.html', {'borrowed_books': borrowed_books})

# View to borrow a book
@login_required
def borrow_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BorrowBookForm(request.POST, instance=book)
        if form.is_valid():
            book.borrower = request.user
            book.borrowed_copies += 1
            form.save()
            return redirect('user_dashboard')
    else:
        form = BorrowBookForm(instance=book)
    return render(request, 'library/borrow_book.html', {'form': form, 'book': book})

# View to extend the due date of a borrowed book
@login_required
def extend_due_date(request, pk):
    book = get_object_or_404(Book, pk=pk, borrower=request.user)
    if request.method == 'POST':
        form = BorrowBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('user_dashboard')
    else:
        form = BorrowBookForm(instance=book)
    return render(request, 'library/extend_due_date.html', {'form': form, 'book': book}) 

# View to return a borrowed book
@login_required
def return_book(request, pk):
    book = get_object_or_404(Book, pk=pk, borrower=request.user)
    if request.method == 'POST':
        book.borrower = None
        book.borrowed_copies -= 1
        book.borrow_date = None
        book.due_date = None
        book.save()
        return redirect('user_dashboard')
    return render(request, 'library/return_book.html', {'book': book})

# View for user login
def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book_list')
    else:
        form = AuthenticationForm()
    return render(request, 'library/signin.html', {'form': form})

# View for user sign-up
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'library/signup.html', {'form': form})    