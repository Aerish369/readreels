from django.contrib import admin
from .models import Author, Book, Collection, Review, Tag, Profile


admin.site.register(Author)
admin.site.register(Profile)
admin.site.register(Collection)
admin.site.register(Review)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['tag']
    }