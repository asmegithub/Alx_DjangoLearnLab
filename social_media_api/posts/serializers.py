from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    # comments will be fetched as nested objects
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def validate(self, data):
        if 'title' in data and len(data['title']) < 5:
            raise serializers.ValidationError(
                "Title must be at least 5 characters long.")
        return data


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

    def validate(self, data):
        if 'content' in data and len(data['content']) < 10:
            raise serializers.ValidationError(
                "Content must be at least 10 characters long.")
        return data
