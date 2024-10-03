from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('books/', views.book_list, name='book_list'),
    path('book/new/', views.book_create, name='book_create'),
    path('book/<int:pk>/edit/', views.book_update, name='book_update'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('book/<int:pk>/borrow/', views.borrow_book, name='borrow_book'),
    path('book/<int:pk>/extend/', views.extend_due_date, name='extend_due_date'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('signin/', views.signin_view, name='sgnin'),
    path('signup/', views.signup_view, name='signup'),
]

