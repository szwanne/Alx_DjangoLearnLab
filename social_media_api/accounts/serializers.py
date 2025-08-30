from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# Serializer to view user data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'bio', 'profile_picture', 'followers']

# Serializer for user registration


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Use the model's built-in method to create user
        return User.objects.create_user(**validated_data)
