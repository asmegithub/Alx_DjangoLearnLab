from rest_framework import serializers

from posts.models import Post
from posts.serializers import PostSerializer
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    recipient = serializers.ReadOnlyField(source='recipient.username')
    actor = serializers.ReadOnlyField(source='actor.username')
    # Custom field for serializing the target
    target = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb',
                  'target', 'timestamp']

    def get_target(self, obj):
        """
        Custom method to serialize the target of the notification.
        It checks the type of the target and returns the appropriate serialized data.
        """
        target_obj = obj.target
        if isinstance(target_obj, Post):
            # Assuming the target is a Post object
            return PostSerializer(target_obj).data
        # Add other models here (e.g., Comment, Photo) if needed
        # Fallback: Return string representation if no serializer exists
        return str(target_obj)
