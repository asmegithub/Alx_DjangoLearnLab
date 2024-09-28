from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # # filtering by title and content
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title', 'content']

    # # search by title and content
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
# this method is called when a new post is created, and used to associate the post with the user who created it

    def perform_create(self, serializer):
        # N.B auther is the name of the field in the Post model
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
# this method is called when a new comment is created, and used to associate the comment with the user who created it

    def perform_create(self, serializer):
        # N.B auther is the name of the field in the Comment model
        serializer.save(author=self.request.user)
