from django.urls import path
from django.conf import settings
from . import views



urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('book-detail/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('book-detail/<int:pk>/delete-review/', views.delete_review,name='delete-review'), 
    path('book-detail/<int:pk>/save-book', views.save_book, name='save-book'),
    path('profile-edit/', views.ProfileView.as_view(), name='profile-edit'),
]