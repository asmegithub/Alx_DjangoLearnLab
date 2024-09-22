from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from .models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    # cusomize the fields to be serialized here

    class Meta:
        model = CustomUser
        fields = '__all__'
    # validation will be done here

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters long.")
        return value


# ["from rest_framework.authtoken.models import Token", "serializers.CharField()", "Token.objects.create", "get_user_model().objects.create_user"]
