from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = '/home/'
    redirect_authenticated_user = True

    

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



