from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages  # Import Django's messaging framework
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from .models import Book, Member  # Import Book and Member models
from .forms import UserRegisterForm, UserAuthenticationForm, BorrowForm, ReturnForm, ExtendForm
# from .forms import BookForm, MemberForm, BorrowForm, ReturnForm, ExtendForm  # Import forms
# Home view
def home(request):
    return render(request, 'library/home.html')

# Sign-up view
def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})

# Sign-in view
def signin_view(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserAuthenticationForm()
    return render(request, 'signin.html', {'form': form})

# Book list view
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

# Borrow book view
@login_required
def borrow_book(request):
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            isbn = form.cleaned_data['isbn']
            book = get_object_or_404(Book, isbn=isbn)
            book.borrower = request.user
            book.borrow_date = form.cleaned_data['borrow_date']
            book.due_date = form.cleaned_data['due_date']
            book.save()
            messages.success(request, f'The book "{book.title}" has been borrowed.')
            return redirect('book_list')
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        form = BorrowForm()
    return render(request, 'library/borrow_book.html', {'form': form})

# Return book view
@login_required
def return_book(request):
    if request.method == 'POST':
        form = ReturnForm(request.POST)
        if form.is_valid():
            isbn = form.cleaned_data['isbn']
            book = get_object_or_404(Book, isbn=isbn)
            book.borrower = None
            book.borrow_date = None
            book.due_date = None
            book.save()
            messages.success(request, f'The book "{book.title}" has been returned.')
            return redirect('book_list')
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        form = ReturnForm()
    return render(request, 'library/return_book.html', {'form': form})

# Extend due date view
@login_required
def extend_due_date(request):
    if request.method == 'POST':
        form = ExtendForm(request.POST)
        if form.is_valid():
            isbn = form.cleaned_data['isbn']
            book = get_object_or_404(Book, isbn=isbn)
            book.due_date = form.cleaned_data['due_date']
            book.save()
            messages.success(request, f'The due date for the book "{book.title}" has been extended to {book.due_date}.')
            return redirect('book_list')
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        form = ExtendForm()
    return render(request, 'library/extend_due_date.html', {'form': form})