from rest_framework import serializers
from .models import Author, Book
import datetime


# Book Serializer: serializes all fields and validates publication_year
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation to ensure the publication year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future.")
        return value


# Author Serializer: includes nested BookSerializer
class AuthorSerializer(serializers.ModelSerializer):
    # "books" is the related_name in the Book model
    # BookSerializer: Serializes all fields of Book.
    # Includes validation to check publication year is not in the future.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
