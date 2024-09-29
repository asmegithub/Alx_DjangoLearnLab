from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from .models import Notification
from .serializers import NotificationSerializer
from .permissions import IsOwnerOrReadOnly


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
# The NotificationViewSet class is a viewset that provides the basic actions for the Notification model. It inherits from viewsets.ModelViewSet, which provides the default set of CRUD actions for a model.
