from django.shortcuts import get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# django's generic views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# rest_framework's generic views
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.permissions import IsAuthenticated

from .forms import CustomUserCreationForm, UserUpdateForm, UserProfileUpdateForm, PostForm, PostUpdateForm

from .models import Post


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


class LoginView(LoginView):
    template_name = 'blog/login.html'


class Post_List(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']


class Post_Detail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
        else:
            return render(request, 'blog/post_form.html', {'form': form})
    else:
        form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form})

# For class base view, use method_decorator to apply login_required decorator to class based views


@method_decorator(login_required, name='dispatch')
class Post_Update(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    fields = ['title', 'content']
    # Make sure 'post_list' is defined in your URL patterns
    success_url = reverse_lazy('post_list')

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        if post.author != self.request.user:
            raise PermissionDenied
        return post

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(
                self.request, 'You do not have permission to update this post')
        return redirect('post_list')


@method_decorator(login_required, name='dispatch')
class Post_Delete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    # Use reverse_lazy for URL resolution
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(
                self.request, 'You do not have permission to delete this post')
        return redirect('post_list')

    # Develop a view that allows authenticated users to view and edit their profile details. This view should handle POST requests to update user information.
    # Ensure the user can change their email and optionally extend the user model to include more fields like a profile picture or bio.
