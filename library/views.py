from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Book, Member  # Import Book and Member models
from .forms import BookForm, MemberForm, BorrowForm, ReturnForm, ExtendForm  # Import forms

# Home view
# Render the home page
def home(request):
    return render(request, 'library/home.html')

# Book list view
# Retrieve all books from the database
# Render the book list page with the retrieved books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books}) 

# Book detail view
# Retrieve a specific book by its ID or return a 404 error if not found
# Render the book detail page with the retrieved book
def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'library/book_detail.html', {'book': book})

# Member list view
# Retrieve all members from the database
# Render the member list page with the retrieved members
def member_list(request):
    members = Member.objects.all()
    return render(request, 'library/member_list.html', {'members': members})

# Member detail view
# Retrieve a specific member by their ID or return a 404 error if not found
# Render the member detail page with the retrieved member
def member_detail(request, id):
    member = get_object_or_404(Member, id=id)
    return render(request, 'library/member_detail.html', {'member': member})

# Borrow Book
# If the request method is POST, create a form instance with the submitted data
# If the form is valid, save the form data to the database
# Redirect to the book list page after successful borrowing
# If the request method is not POST, create an empty form instance
# Render the borrow book page with the form
def borrow_book(request):
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BorrowForm()  # Initialize the form for GET requests
    # return render(request, 'library/borrow_book.html', {'form': form})
    return render(request, 'admin/borrow_book.html', {'form': form})

# Return book view
# If the request method is POST, create a form instance with the submitted data
# If the form is valid, save the form data to the database
# Redirect to the book list page after successful return
# If the request method is not POST, create an empty form instance
# Render the return book page with the form
def return_book(request):
    if request.method == 'POST':
        form = ReturnForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ReturnForm()
    return render(request, 'library/return_book.html', {'form': form})

# Extend due date view
# If the request method is POST, create a form instance with the submitted data
# If the form is valid, save the form data to the database
# Redirect to the book list page after successful extension
# If the request method is not POST, create an empty form instance
# Render the extend due date page with the form
def extend_due_date(request):
    if request.method == 'POST':
        form = ExtendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ExtendForm()
    return render(request, 'library/extend_due_date.html', {'form': form})

# Sign-up view
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, user) 
            return redirect('home') # Redirect to home page 
        else:
            form = AuthenticationForm()
        return render(request, 'signin.html', {'form':form})         

# sign-in view
def signin_view(request):
    if request.method == 'POST'
    form = UserAuthenticationForm(data = request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home')