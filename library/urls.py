from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('books/', views.book_list, name='book_list'),  # Book list page
    path('books/<int:id>/', views.book_detail, name='book_detail'),  # Book detail page
    path('members/', views.member_list, name='member_list'),  # Member list page
    path('members/<int:id>/', views.member_detail, name='member_detail'),  # Member detail page
]