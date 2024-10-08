from django.shortcuts import get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.db.models import Q
# django's generic views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# rest_framework's generic views
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import CustomUserCreationForm, UserUpdateForm, UserProfileUpdateForm, PostForm, CommentForm

from .models import Post, Comment, Tag


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
    # Handling comments in Post_Detail view

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.get_object().comments.all()
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
        return self.get(request, *args, form=form)


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
# this allow only the author of the post to update the post
# if the user is not the author of the post, PermissionDenied will be raised

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
# if the user is authenticated but not the author of the post, this method will be called

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


@login_required
def CommentCreateView(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = get_object_or_404(Post, pk=pk)
            comment.save()
            return redirect('post_detail', pk=pk)
        else:
            return render(request, 'blog/comment_form.html', {'form': form})
    else:
        form = CommentForm()
        return render(request, 'blog/comment_form.html', {'form': form})


class CommentListView(ListView):
    model = Comment
    template_name = 'blog/comment_list.html'
    context_object_name = 'comments'
    ordering = ['-created_at']

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['post'] = get_object_or_404(
    #         Post, pk=self.kwargs.get('pk'))
    #     return context


class CommentDetailView(DetailView):
    model = Comment
    template_name = 'blog/comment_detail.html'


# for class based views, use method_decorator to apply login_required decorator to class based views


@method_decorator(login_required, name='dispatch')
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = 'blog/comment_form.html'
    fields = ['content']
    success_url = reverse_lazy('comment_list')

    def get_object(self, queryset=None):
        return Comment.objects.get(pk=self.kwargs.get('pk'))

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(
                self.request, 'You do not have permission to update this comment')
        return redirect('comment_list')


@method_decorator(login_required, name='dispatch')
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'
    success_url = reverse_lazy('comment_list')

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(
                self.request, 'You do not have permission to delete this comment')
        return redirect('comment_list')


def search_view(request):
    query = request.GET.get('q', '')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.none()

    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})


def posts_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = Post.objects.filter(tags=tag)
    return render(request, 'blog/posts_by_tag.html', {'posts': posts, 'tag': tag_name})


class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list_by_tag.html'

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')
        return Post.objects.filter(tags__slug=tag_slug)
