from django import forms  # Import Django's forms module
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Book, Member  # Import the Book and Member models from the current app

# Form for the Book model
class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # Specify the model to use
        fields = ['title', 'author', 'published_date', 'isbn']  # Specify the fields to include in the form, matching the Book model

# Form for the Member model
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member  # Specify the model to use
        fields = ['first_name', 'last_name', 'email', 'join_date']  # Specify the fields to include in the form, matching the Member model

# Form for user registration
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Form for user authentication
class UserAuthenticationForm(AuthenticationForm):
    pass

# Form for borrowing a book
class BorrowForm(forms.ModelForm):
    class Meta:
        model = Book  # Specify the model to use
        fields = ['title', 'author', 'borrower', 'borrow_date', 'due_date']  # Specify the fields to include in the form

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not Book.objects.filter(isbn=isbn).exists():
            raise forms.ValidationError("Book with this ISBN does not exist.")
        return isbn

# Form for returning a book
class ReturnForm(forms.ModelForm):
    class Meta:
        model = Book  # Specify the model to use
        fields = ['isbn']  # Specify the fields to include in the form

# Form for extending the due date of a borrowed book
class ExtendForm(forms.ModelForm):
    class Meta:
        model = Book  # Specify the model to use
        fields = ['isbn', 'due_date']  # Specify the fields to include in the form

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not Book.objects.filter(isbn=isbn).exists():
            raise forms.ValidationError("Book with this ISBN does not exist.")
        return isbn