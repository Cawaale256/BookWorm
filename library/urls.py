from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from django.urls import path
from library.views import debug_view  # adjust if your view is elsewhere

urlpatterns = [
    path('debug/', debug_view, name='debug'),
]


urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('books/', views.book_list, name='book_list'),
    path('book/new/', views.book_create, name='book_create'),
    path('book/<int:pk>/edit/', views.book_update, name='book_update'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('book/<int:pk>/borrow/', views.borrow_book, name='borrow_book'),
    path('book/<int:pk>/extend/', views.extend_due_date, name='extend_due_date'),
    path('book/<int:pk>/return/', views.return_book, name='return_book'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('signin/', views.signin_view, name='signin_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('signout/', auth_views.LogoutView.as_view(next_page='signin_view'), name='signout_view'),
    path('members/', views.member_list, name='member_list'),
    path('members/<int:pk>/', views.member_profile, name='member_profile'),
    path('members/<int:pk>/edit/', views.edit_member, name='edit_member'),
]