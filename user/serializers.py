from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from djoser.serializers import UserCreatePasswordRetypeSerializer, TokenCreateSerializer
from rest_framework import serializers

from .models import User
from .validators import validate_password


class UsersCreateSerializer(UserCreatePasswordRetypeSerializer):
    """Сериализатор регистрации"""
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'middle_name', 'email', 'phone', 'password')

    def validate(self, attrs):
        username = f'{attrs["phone"]}'
        attrs['username'] = username
        attrs = super().validate(attrs)
        return attrs

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(exc)
        return value
