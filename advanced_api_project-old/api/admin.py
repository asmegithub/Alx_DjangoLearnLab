from django.contrib import admin
from django import forms
from datetime import datetime

from .models import Author, Book


class CustomAuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_books']

    def get_books(self, obj):
        return ", ".join([book.title for book in obj.books.all()])

    get_books.short_description = 'Books'  # Optional: Name for the column


# Custom form for Book model to add validation
# The admin interface uses this form to create and update Book instances,it does not use the serializer
class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    # Add validation for the publication_year field
    def clean_publication_year(self):
        publication_year = self.cleaned_data.get('publication_year')
        current_year = datetime.now().year
        if publication_year > current_year:
            raise forms.ValidationError(
                "Publication year must be before or equal to the current year")
        return publication_year


class CustomBookAdmin(admin.ModelAdmin):
    form = BookAdminForm
    list_display = ['title', 'publication_year', 'author']


admin.site.register(Author, CustomAuthorAdmin)
admin.site.register(Book, CustomBookAdmin)
