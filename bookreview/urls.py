from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('book-detail/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('book-detail/<int:pk>/delete-review/', views.delete_review,name='delete_review'), 
    path('profile-edit/', views.ProfileView.as_view(), name='profile-edit')
]