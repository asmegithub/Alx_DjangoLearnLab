from rest_framework import serializers

from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    # ReadOnlyField means it does not allow clients to set or change the author through the API.
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    # queryset argument is required unless it is read_only !!

    class Meta:
        model = Comment
        fields = ['id', 'content', 'post',
                  'author', 'created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    # Nested serializer
    comments = CommentSerializer(
        many=True, read_only=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author',
                  'comments', 'created_at', 'updated_at']
