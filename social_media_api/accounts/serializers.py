from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from .models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    # fields to be serialized/deserialized
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    bio = serializers.CharField()
    profile_picture = serializers.ImageField()
    followers = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)
    password = serializers.CharField(write_only=True)
    # posts = serializers.PrimaryKeyRelatedField(
    #     many=True, read_only=True,queryset=Snippet.objects.all())
    # CRUD operations are defined here

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters long.")
        return value
