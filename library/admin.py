from django.contrib import admin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import path
from django.utils.html import format_html
from .models import Book, Member
from .forms import BorrowForm, ExtendForm

# Define the admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'isbn')
    # Fields to include in the search functionality
    search_fields = ('title', 'author', 'isbn')

    # Override the get_urls method to add custom URLs
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:book_id>/borrow/', self.admin_site.admin_view(self.borrow_book), name='borrow_book'),
        ]
        return custom_urls + urls

    # Define a custom action for borrowing a book
    def borrow_book_action(self, obj):
        return format_html('<a class="button" href="{}">Borrow</a>', f'/admin/library/book/{obj.id}/borrow/')
    borrow_book_action.short_description = 'Borrow Book'
    borrow_book_action.allow_tags = True

    # Handle the borrowing process
    def borrow_book(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        if request.method == 'POST':
            form = BorrowForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                self.message_user(request, "Book borrowed successfully.")
                return redirect('..')
        else:
            form = BorrowForm(instance=book)
        return render(request, 'admin/borrow_book.html', {'form': form, 'book': book})

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)

# Define the admin class for the Member model
class MemberAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('first_name', 'last_name', 'email', 'join_date')
    # Fields to include in the search functionality
    search_fields = ('first_name', 'last_name', 'email')

# Register the Member model with the custom admin class
admin.site.register(Member, MemberAdmin)