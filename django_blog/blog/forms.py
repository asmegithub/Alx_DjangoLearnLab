from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from taggit.forms import TagWidget

from taggit.forms import TagField
from .models import UserProfile, Post, Comment


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


class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=TagWidget(), required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


class PostUpdateForm(forms.ModelForm):
    tags = TagField()  # Add this line for tags

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    # You can add custom validation here

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError('Content cannot be empty.')
        if len(content) < 10:
            raise forms.ValidationError(
                'Content must be at least 10 characters long.')
        return content


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)
