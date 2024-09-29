from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.decorators import action

from notifications.models import Notification
from .models import Like

from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .models import Post, Comment, Like
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
# posts/feed

    @action(detail=False, methods=['get'])
    def feed(self, request,):
        # get all the posts of the user and the users that the user is following
        user = request.user
        # feteching associated following users for the current user
        following_users = user.following.all()
        # fetching the posts of the following users
        posts = Post.objects.filter(
            author__in=following_users).order_by('-created_at')
        # Post.objects.filter(author__in=following_users).order_by", "following.all()
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

# /posts/1/like
    @action(detail=True, methods=['get'])
    def like(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)
        likes, created = Like.objects.get_or_create(
            user=request.user, post=post)
        if created:
            notification = Notification.objects.create(
                recipient=post.author, actor=request.user, verb='liked', target=post)
            notification.save()
            return Response(f'{request.user.username} just liked {post.title}')
        else:
            return Response("you have already liked this post")
    # /posts/1/unlike

    @action(detail=True, methods=['get'])
    def unlike(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user
        likes = Like.objects.filter(user=user, post=post)
        if likes.exists():
            likes.delete()
            notification = Notification.objects.create(
                recipient=post.author, actor=user, verb='unliked', target=post)
            notification.save()
            serializer = LikeSerializer(likes, many=True)
            return Response(serializer.data)
        else:
            return Response("you have not liked this post")


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
# this method is called when a new comment is created, and used to associate the comment with the user who created it

    def perform_create(self, serializer):
        # N.B auther is the name of the field in the Comment model
        serializer.save(author=self.request.user)

# this will be deleted later


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def like(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        likes = Like.objects.filter(post=post)
        user = request.user
        existing_user = likes.filter(user=user)

        if existing_user.exists():
            existing_user.delete()
            notification = Notification.objects.create(
                recipient=post.author, actor=user, verb='unliked', target=post)
            notification.save()
            print("you have unliked this post: ", notification)
            serializer = LikeSerializer(likes, many=True)
            return Response(serializer.data)
        else:
            like = Like.objects.create(post=post, user=user)
            notification = Notification.objects.create(
                recipient=post.author, actor=user, verb='liked', target=post)
            like.save()
            notification.save()
            print("you have liked this post")
            serlizer = LikeSerializer(likes, many=True)
            return Response(serlizer.data)
