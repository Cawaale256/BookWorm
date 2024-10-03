from django.contrib import admin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import path
from django.utils.html import format_html
from .models import Book, Member
from .forms import BorrowForm, ExtendForm

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn')  # Removed 'published_date'
    search_fields = ('title', 'author', 'isbn')
admin.site.register(Book, BookAdmin)

# Define a custom action for borrowing a book
def borrow_book_action(self, obj):
    return format_html('<a class="button" href="{}">Borrow</a>', f'/admin/library/book/{obj.id}/borrow/')
borrow_book_action.short_description = 'Borrow Book'
borrow_book_action.allow_tags = True    

class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'join_date')
    search_fields = ('first_name', 'last_name', 'email')
admin.site.register(Member, MemberAdmin)