from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from .forms import CustomUserCreationForm, UserUpdateForm, UserProfileUpdateForm


def home(request):
    return render(request, 'blog/base.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
        else:
            messages.error(request, 'Error creating account')
            return render(request, 'blog/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'blog/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'blog/profile.html', context)


# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Profile updated successfully!')
#             return redirect('profile')
#         else:
#             messages.error(request, 'Error updating profile')
#             return render(request, 'blog/edit_profile.html', {'form': form})
#     else:
#         form = CustomUserCreationForm(instance=request.user)
#         return render(request, 'blog/edit_profile.html', {'form': form})


class LoginView(LoginView):
    template_name = 'blog/login.html'


# Develop a view that allows authenticated users to view and edit their profile details. This view should handle POST requests to update user information.
# Ensure the user can change their email and optionally extend the user model to include more fields like a profile picture or bio.
