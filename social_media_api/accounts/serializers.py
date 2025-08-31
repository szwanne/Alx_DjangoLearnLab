# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import User


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # Use Django's built-in create_user to handle password hashing
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        # Automatically create token for the user
        Token.objects.create(user=user)
        return user


class UserSerializer(serializers.ModelSerializer):
    following_count = serializers.IntegerField(
        source='following.count', read_only=True)
    followers_count = serializers.IntegerField(
        source='followers.count', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'following_count', 'followers_count']
