from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    # cusomize the fields to be serialized here
    class Meta:
        model = CustomUser
        fields = '__all__'
    # validation will be done here
