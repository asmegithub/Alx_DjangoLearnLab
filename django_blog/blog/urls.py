from django.urls import path
from django.contrib.auth.views import LogoutView


from .views import LoginView, register, profile, home

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    # path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/', profile, name='profile'),

    path('logout/', LogoutView.as_view(), name='logout'),
]
