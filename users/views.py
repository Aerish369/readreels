from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = '/home/'
    redirect_authenticated_user = True

    

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
