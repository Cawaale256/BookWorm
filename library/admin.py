from django.contrib import admin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import path
from django.utils.html import format_html
from .models import Book, Member
from .forms import BorrowBookForm, ExtendForm

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'borrow_book_action')
    search_fields = ('title', 'author', 'isbn')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:book_id>/borrow/', self.admin_site.admin_view(self.borrow_book), name='borrow_book'),
        ]
        return custom_urls + urls

    def borrow_book_action(self, obj):
        return format_html('<a class="button" href="{}">Borrow</a>', f'/admin/library/book/{obj.id}/borrow/')
    borrow_book_action.short_description = 'Borrow Book'
    borrow_book_action.allow_tags = True

    def borrow_book(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        if request.method == 'POST':
            form = BorrowBookForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                self.message_user(request, "Book borrowed successfully.")
                return redirect('..')
        else:
            form = BorrowBookForm(instance=book)
        return render(request, 'admin/borrow_book.html', {'form': form, 'book': book})

admin.site.register(Book, BookAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'join_date')
    search_fields = ('first_name', 'last_name', 'email')

admin.site.register(Member, MemberAdmin)