from typing import Any
from django.contrib.auth.views import RedirectURLMixin
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


# class BookListView(ListView):
#     template_name = 'bookreview/home.html'
    
#     def get_queryset(self) -> QuerySet[Any]:
#         return Book.objects\
#                 .select_related('Author')\
#                 .all()

#! Now make the Profile view in a way that it could edit the fields of the user associated with it. 

class ProfileView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'bookreview/profile.html'
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
        profile_form = ProfileForm(request.POST, instance=self.get_object())

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect(self.success_url)
        
        return self.get(request, *args, **kwargs)