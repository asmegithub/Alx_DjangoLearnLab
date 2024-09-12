from rest_framework import serializers
from datetime import datetime
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    # Display author's name when retrieving data
    author_name = serializers.CharField(source='author.name', read_only=True)
    # Allow setting author by ID when creating/updating
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        # Ensure the publication year is not in the future
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year must be before or equal to the current year"
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    # Serializer for the Author model

    # Nested serializer to include books related to the author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
