from django.contrib import admin
from .models import Book, Member

# Register the Book model with the admin site
admin.site.register(Book)

# Register the Member model with the admin site
admin.site.register(Member)