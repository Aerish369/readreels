from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    # path('home/', views.BookListView.as_view(), name='home'),
    path('profile/', views.ProfileView.as_view(), name='profile')
]