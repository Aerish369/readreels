from typing import Any
from django.contrib.auth.views import RedirectURLMixin
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Book, Profile
from .forms import ProfileForm
from users.forms import CustomUserCreationForm
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
    fields = ['birth_date', 'bio', 'profile_image']
    template_name = 'bookreview/profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user.profile 
    
    # def post(self, *args, **kwargs):
    #     User = settings.AUTH_USER_MODEL
    #     form = CustomUserCreationForm(self.request.POST, instance=User.objects.get(id=self.request.user.id))
    #     if form.is_valid():
    #         return self.form_valid(form)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['first_name'] = self.request.user.first_name
        context['last_name'] = self.request.user.last_name
        context['username'] = self.request.user.username
        context['email'] = self.request.user.email

        return context