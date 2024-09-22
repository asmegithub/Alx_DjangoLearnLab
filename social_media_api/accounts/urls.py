from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import register, LoginView, ProfileDetailView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
