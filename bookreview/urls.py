from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('book-detail/<slug:slug>/', views.BookDetailView.as_view(), name='book-detail'),
    path('profile-edit/', views.ProfileView.as_view(), name='profile-edit')
]