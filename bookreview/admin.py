from django.contrib import admin
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.http import HttpRequest
from . import models



@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'reviewed_count', 'created_at']
    list_per_page = 20
    list_select_related = ['user']
    ordering = ['user__username', 'user__first_name', 'user__last_name']
    search_fields = ['user__username__istartswith', 'user__first_name__istartswith', 'user__last_name__istartswith']

    def reviewed_count(self, profile):
        return profile.user.review_set.count()
 

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 20
    search_fields = ['name__istartswith']
    ordering = ['name']


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'tag', 'review_count', 'isbn', 'publication_date'] 
    list_per_page = 20
    list_select_related = ['author', 'tag'] 
    ordering = ['title', 'author']
    search_fields = ['title__istartswith']
    prepopulated_fields = {
        'slug': ['title']
    }

    @admin.display(ordering='review_count')
    def review_count(self, book):
        return book.review_set.count()

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            review_count= Count('review')
        )


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['reviewer', 'reviewed_book', 'rating', 'review_date']
    list_per_page = 20

    @admin.display(ordering='reviewed_book')
    def reviewed_book(self, review):
        return review.book.title


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_public', 'created_date']


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag']
    prepopulated_fields = {
        'slug': ['tag']
    }