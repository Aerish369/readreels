from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile-edit/', views.ProfileView.as_view(), name='profile-edit')
]