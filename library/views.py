from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm, BorrowForm, ExtendForm

def home(request):
    books = Book.objects.all()
    return render(request, 'library/home.html', {'books': books})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

@login_required
def book_create(request):
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to create books.")
        return redirect('book_list')
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book created successfully.")
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', {'form': form})

@login_required
def book_update(request, pk):
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to update books.")
        return redirect('book_list')
    
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully.")
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/book_form.html', {'form': form})

@login_required
def book_delete(request, pk):
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to delete books.")
        return redirect('book_list')
    
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book deleted successfully.")
        return redirect('book_list')
    return render(request, 'library/book_confirm_delete.html', {'book': book})

@login_required
def user_dashboard(request):
    borrowed_books = Book.objects.filter(borrower=request.user)
    return render(request, 'library/user_dashboard.html', {'borrowed_books': borrowed_books})

@login_required
def borrow_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BorrowForm(request.POST, instance=book)
        if form.is_valid():
            book.borrower = request.user
            book.borrowed_copies += 1
            form.save()
            messages.success(request, "Book borrowed successfully.")
            return redirect('home')
    else:
        form = BorrowForm(instance=book)
    return render(request, 'library/borrow_book.html', {'form': form, 'book': book})

@login_required
def extend_due_date(request, pk):
    book = get_object_or_404(Book, pk=pk, borrower=request.user)
    if request.method == 'POST':
        form = ExtendForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Due date extended successfully.")
            return redirect('home')
    else:
        form = ExtendForm(instance=book)
    return render(request, 'library/extend_due_date.html', {'form': form, 'book': book})

@login_required
def return_book(request, pk):
    book = get_object_or_404(Book, pk=pk, borrower=request.user)
    if request.method == 'POST':
        book.borrower = None
        book.borrowed_copies -= 1
        book.borrow_date = None
        book.due_date = None
        book.save()
        messages.success(request, "Book returned successfully.")
        return redirect('home')
    return render(request, 'library/return_book.html', {'book': book})

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

def signout_view(request):
    logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect('signin_view')    