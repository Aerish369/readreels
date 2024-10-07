from django.contrib import admin
from .models import Author, Book, Collection, Review, Tag, Profile


admin.site.register(Author)
# admin.site.register(Book)
admin.site.register(Profile)
admin.site.register(Collection)
admin.site.register(Review)
admin.site.register(Tag) 

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }