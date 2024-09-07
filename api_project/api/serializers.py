from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    # custumization field goes here
    class Meta:
        model = Book
        fields = "__all__"
# validation goes here
