from django.urls import path
from django.conf import settings
from django.views.generic import TemplateView
from . import views



urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('book-detail/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('book-detail/<int:pk>/delete-review/', views.DeleteReviewView.as_view(),name='delete-review'), 
    path('book-detail/<int:pk>/save-book', views.SaveBookView.as_view(), name='save-book'),
    path('profile-edit/', views.ProfileView.as_view(), name='profile-edit'),
    path('about/', TemplateView.as_view(template_name='bookreview/about.html'), name='about'),
]