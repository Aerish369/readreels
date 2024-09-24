from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm

class CustomLoginView(LoginView):
    '''View for logging in a user.'''
    template_name = 'registration/login.html'
    success_url = '/home/'
    redirect_authenticated_user = True

    

class CustomLogoutView(LogoutView):
    '''View for logging out a user.'''
    next_page = reverse_lazy('login')


class SignUpView(SuccessMessageMixin, CreateView):
    '''View for signing up a new user.'''
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home') #! Later redirect to profile page
    template_name = 'registration/signup.html'
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        '''If the form is valid, save the associated model.'''
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


