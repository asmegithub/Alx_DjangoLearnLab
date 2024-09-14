from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']


class CustomUserCreationForm(UserCreationForm):
    # You can add more fields that are not in UserCreationForm here, if you want to store more information
    # But all the fields defined here will not be migrated to database,
    bio = forms.CharField(max_length=500, required=False)

    class Meta(UserCreationForm.Meta):
        model = UserCreationForm.Meta.model
        # for fields in defualt built-in User model and are not visible by defualt in UserCreationForm, you can add them here without any need of redifining it above.
        fields = UserCreationForm.Meta.fields + ('email', 'bio')
