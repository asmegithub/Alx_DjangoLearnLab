from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib import admin
from .models import Book

# admin.site.register(Book)


class CustomBookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
    fields = ('title', 'author', 'publication_year')


admin.site.register(Book, CustomBookAdmin)


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'date_of_birth', 'profile_photo', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),)


admin.site.register(CustomUser, CustomUserAdmin)
