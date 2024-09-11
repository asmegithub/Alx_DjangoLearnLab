import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['icontains'],  # Allows searching by partial title

            # Allows filtering by year and range
            'publication_year': ['exact', 'lte', 'gte'],

        }
