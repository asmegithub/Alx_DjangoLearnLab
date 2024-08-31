from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin


class UserAdmin(CustomUserAdmin):
    list_display = ('username', 'date_of_birth', 'profile_photo')


admin.site.register(CustomUser, UserAdmin)
