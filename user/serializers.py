from django.core.exceptions import ValidationError
from djoser.serializers import UserCreatePasswordRetypeSerializer
from rest_framework import serializers

from .models import User
from .validators import validate_password


class UsersCreateSerializer(UserCreatePasswordRetypeSerializer):
    """Serialization to create user data"""
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'middle_name', 'email', 'phone', 'password')

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(exc)
        return value
