from django.contrib import admin
from .models import Author, Book, Collection, Review, Tag


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Collection)
admin.site.register(Review)
admin.site.register(Tag)