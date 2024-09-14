from django.urls import path
from django.contrib.auth.views import LogoutView


from .views import LoginView, register, profile, home, Post_List, Post_Detail, post_create, Post_Update, Post_Delete
from .views import Post_Update

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),

    #
    path('posts/', Post_List.as_view(), name='post_list'),
    path('posts/<int:pk>/', Post_Detail.as_view(), name='post_detail'),
    path('post/new/', post_create, name='post_new'),
    path('post/<int:pk>/update/', Post_Update.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', Post_Delete.as_view(), name='post_delete'),


]
