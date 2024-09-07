from django.urls import path, include

from .views import BookViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books', BookViewSet, basename='book')

urlpatterns = [
    # since router.urls give an array of all the urls for the viewset so we should use "include"
    path('', include(router.urls)),
]
