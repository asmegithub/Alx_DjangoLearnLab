from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action

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

    @action(detail=False, methods=['get'])
    def feeds(self, request,):
        # get all the posts of the user and the users that the user is following
        user = request.user
        # feteching associated following users for the current user
        following_users = user.followings.all()
        # fetching the posts of the following users
        posts = Post.objects.filter(
            author__in=following_users).order_by('-created_at')
        # Post.objects.filter(author__in=following_users).order_by", "following.all()
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
# this method is called when a new comment is created, and used to associate the comment with the user who created it

    def perform_create(self, serializer):
        # N.B auther is the name of the field in the Comment model
        serializer.save(author=self.request.user)
