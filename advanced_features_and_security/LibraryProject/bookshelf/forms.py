from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Book, CustomUser


class CustomUserCreationForm(UserCreationForm):
    ROLES = [
        ('viewers', 'Viewers'),
        ('admins', 'Admins'),
        ('editors', 'Editors'),
    ]
    role = forms.ChoiceField(choices=ROLES, required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'date_of_birth',
                  'profile_photo', 'password1', 'password2')


class CustomBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
