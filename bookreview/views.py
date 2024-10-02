from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Book, Profile
from .forms import ProfileForm, UserProfileForm
from django.conf import settings


def home(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request, "bookreview/home.html", context)


class ProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'bookreview/profile_edit.html'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user.profile 
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserProfileForm(instance=self.request.user)
        context['profile_form'] = self.get_form()
        return context
    
    def post(self, request, *args, **kwargs):
        user_form = UserProfileForm(request.POST, instance=self.request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=self.get_object())

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect(self.success_url)
        
        return self.get(request, *args, **kwargs)