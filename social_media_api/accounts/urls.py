from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import register, LoginView, ProfileDetailView, CustomUserViewSet, follow_user, unfollow_user


# follow_user = CustomUserViewSet.as_view({'post': 'follow_user'})
# unfollow_user = CustomUserViewSet.as_view({'post': 'unfollow_user'})

urlpatterns = [
    # routing for accounts
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    # routing for follow and unfollow user
    path('follow/<int:user_id>/', follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
