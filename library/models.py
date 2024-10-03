from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
      title = models.CharField(max_length=200, default='Unknown Title')
      author = models.CharField(max_length=200, default='Unknown Author')
      isbn = models.CharField(max_length=13, unique=True)
      copies = models.PositiveIntegerField(default=1)
      borrowed_copies = models.PositiveIntegerField(default=0)
      borrower = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
      borrow_date = models.DateField(null=True, blank=True)
      due_date = models.DateField(null=True, blank=True)

      def is_available(self):
           return self.copies > self.borrowed_copies

      def __str__(self):
        return self.title

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    join_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"