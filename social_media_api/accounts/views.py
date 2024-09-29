from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework import generics

from .serializers import CustomUserSerializer
from .forms import CustomUserCreationForm

from .models import CustomUser


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, "accounts/register.html", {'form': form})


class LoginView(LoginView):
    template_name = 'accounts/login.html'
    # this allow an already authenticated user to be redirected to the login_redirect page
    redirect_authenticated_user = True


class ProfileDetailView(DetailView):
    model = CustomUser
    template_name = 'accounts/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user


@api_view(['GET'])
def follow_user(request, user_id=None):
    # pk => primary key at CustomUser model, so you can't modify its name
    user_to_follow = get_object_or_404(CustomUser, pk=user_id)
    user_to_follow.followers.add(request.user)
    request.user.following.add(user_to_follow)
    return Response({'status': f'you followed {user_to_follow.username} !'})


@api_view(['GET'])
def unfollow_user(request, user_id=None):
    user_to_unfollow = get_object_or_404(CustomUser, pk=user_id)
    user_to_unfollow.followers.remove(request.user)
    request.user.following.remove(user_to_unfollow)
    return Response({'status': f'You unfollowed {user_to_unfollow.username} !'})


class CustomUserViewSet(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # @action(detail=True, methods=['get'])
    # def follow_user(self, request, pk=None):
    #     user_to_follow = get_object_or_404(CustomUser, pk=pk)
    #     user_to_follow.followers.add(request.user)
    #     return Response({'status': f'you followed {user_to_follow.username} !'})

    # @action(detail=True, methods=['get'])
    # def unfollow_user(self, request, pk=None):
    #     user_to_unfollow = get_object_or_404(CustomUser, pk=pk)
    #     user_to_unfollow.followers.remove(request.user)
    #     return Response({'status': f'You unfollowed {user_to_unfollow.username} !'})
