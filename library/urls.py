from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
path('', views.home, name='home'),  # Home page
    path('signup/', views.signup_view, name='signup'),#signup
    path('signin/', views.signin_view, name='signin'),# signin
    path('logout/', LogoutView.as_view(), name='logout'), # logout
    path('books/', views.book_list, name='book_list'),  # Book list page
    path('books/<int:id>/', views.book_detail, name='book_detail'),  # Book detail page
    path('members/', views.member_list, name='member_list'),  # Member list page
    path('members/<int:id>/', views.member_detail, name='member_detail'),  # Member detail page
    path('borrow/', views.borrow_book, name='borrow_book'),  # Borrow book page
    path('return/', views.return_book, name='return_book'),  # Return book page
    path('extend/', views.extend_due_date, name='extend_due_date'),  # Extend due date page
]