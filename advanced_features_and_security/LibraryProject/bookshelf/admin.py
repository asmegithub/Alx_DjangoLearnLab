from django.contrib.auth.admin import UserAdmin as CustomUserAdmin
from .models import CustomUser
from django.contrib import admin
from .models import Book

admin.site.register(Book)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')


class UserAdmin(CustomUserAdmin):
    list_display = ('username', 'date_of_birth', 'profile_photo')


admin.site.register(CustomUser, UserAdmin)
