from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

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
    # redirect_authenticated_user = True


class ProfileDetailView(DetailView):
    model = CustomUser
    template_name = 'accounts/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user
