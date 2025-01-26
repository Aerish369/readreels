import django_filters 
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
                    field_name='title', 
                    lookup_expr='icontains',
                    label=''
                    )

    class Meta:
        model = Book
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields['title'].widget.attrs.update({
            'class': 'form-control mr-sm-2',
            'type': 'search',
            'placeholder': 'Search',
            'aria-label': 'Search',
        })