from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LogoutView
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
# Borrow book view
def borrow_book(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Create a form instance with the POST data
        form = BorrowForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Get the title from the cleaned data
            title = form.cleaned_data['title']
            # Get the author from the cleaned data
            author = form.cleaned_data['author']
            # Retrieve the book with the provided title and author
            book = get_object_or_404(Book, title=title, author=author)
            # Update the book's borrower information
            book.borrower = form.cleaned_data['borrower']
            # Update the book's borrow date
            book.borrow_date = form.cleaned_data['borrow_date']
            # Update the book's due date
            book.due_date = form.cleaned_data['due_date']
            # Save the updated book information
            book.save()
            # Redirect to the book list page after successful borrowing
            return redirect('book_list')
        else:
            # Print form errors for debugging
            print("Form errors:", form.errors)
    else:
        # Create an empty form instance
        form = BorrowForm()
    # Render the borrow book form using the correct template path
    return render(request, 'library/borrow_book.html', {'form': form})

# Return book view
def return_book(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Create a form instance with the POST data
        form = ReturnForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Get the ISBN from the cleaned data
            isbn = form.cleaned_data['isbn']
            # Retrieve the book with the provided ISBN
            book = get_object_or_404(Book, isbn=isbn)
            # Update the book's return information
            book.return_date = form.cleaned_data['return_date']
            # Clear the borrower field
            book.borrower = None
            # Clear the borrow date field
            book.borrow_date = None
            # Clear the due date field
            book.due_date = None
            # Save the updated book information
            book.save()
            # Redirect to the book list page after successful return
            return redirect('book_list')
        else:
            # Print form errors for debugging
            print("Form errors:", form.errors)
    else:
        # Create an empty form instance
        form = ReturnForm()
    # Render the return book form using the correct template path
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
        return render(request, 'signup.html', {'form':form})         

# sign-in view
def signin_view(request):
    if request.method =='POST':
        form = UserAuthenticationForm(data = request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form':form})        