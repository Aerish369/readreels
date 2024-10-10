from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, DetailView
from typing import Any

from .models import Book, Profile, Review
from .forms import ProfileForm, UserProfileForm, ReviewForm



class HomeView(ListView):
    model = Book
    template_name = 'bookreview/home.html'
    context_object_name = 'books'



class BookDetailView(LoginRequiredMixin, DetailView, UpdateView):
    model = Book
    template_name = 'bookreview/book_detail.html'
    login_url = reverse_lazy('login')

    form_class = ReviewForm


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        book = self.object

        user_review = Review.objects.filter(book=book, reviewer=self.request.user).first()

        if user_review:
            context['review_form'] = ReviewForm(instance=user_review)
            context['is_reviewed'] = True
        else:
            context['review_form'] = ReviewForm
            context['is_reviewed'] = False
        context['reviews'] = Review.objects.filter(book=book)
        return context
            

    def post(self, request, *args, **kwargs):
        book = self.get_object()
        user = self.request.user

        user_review = Review.objects.filter(book=book, reviewer=self.request.user).first()

        if user_review:
            review_form = ReviewForm(request.POST, instance=user_review)
        else:
            review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.reviewer = user
            review.book = book
            review.save()
            return redirect(request.path)
        context = self.get_context_data(**kwargs)
        context['review_form'] = review_form  
        return self.render_to_response(context)



@login_required
def delete_review(request, pk):
    book = get_object_or_404(Book, id=pk)
    review = Review.objects.get(book=book, reviewer=request.user)

    if request.method == 'POST':
        review.delete()
    return HttpResponseRedirect(reverse('book-detail', kwargs={'pk': book.id}))

@login_required
def save_book(request, pk):
    book = get_object_or_404(Book, id=pk)

    if request.method == 'POST':
        book_id = book.id
        book
    return HttpResponseRedirect(reverse('book-detail', kwargs={'pk': book.id}))



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