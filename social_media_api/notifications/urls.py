from django.urls import path, include
from rest_framework.routers import DefaultRouter
# importing the router instance from the main project
# from social_media_api.urls import router

from .views import NotificationViewSet

router = DefaultRouter()

router.register('notifications', NotificationViewSet,
                basename='notifications')

urlpatterns = [
    path('', include(router.urls)),
]
