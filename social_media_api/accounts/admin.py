from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'bio', 'profile_picture')

    class Meta:
        model = CustomUser
        fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('bio', 'profile_picture', 'followers')}),
        )


admin.site.register(CustomUser, CustomUserAdmin)
