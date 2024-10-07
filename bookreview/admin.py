from django.contrib import admin
from .models import Author, Book, Collection, Review, Tag, Profile


admin.site.register(Profile)
admin.site.register(Collection)
admin.site.register(Review)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # list_display = ['title', 'author', 'tag', 'isbn', 'publication_date'] 
    # list_per_page = 50 
    # list_select_related = ['author', 'tag'] 
    # ordering = ['title', 'author']
    prepopulated_fields = {
        'slug': ['title']
    }

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['tag']
    }