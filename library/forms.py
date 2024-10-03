from django import forms
from .models import Book, Member

# Form for creating and updating Book instances
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # Fields to be included in the form
        fields = ['title', 'author', 'isbn', 'copies', 'borrowed_copies', 'borrower', 'borrow_date', 'due_date']

# Form for creating and updating Member instances
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        # Fields to be included in the form
        fields = ['first_name', 'last_name', 'email', 'join_date']

class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['borrow_date', 'due_date']

# Form for extending the due date of a borrowed book
class ExtendForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['due_date']        