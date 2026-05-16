import re
from typing import Any

from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from apps.users.models import User


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
        ]


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        write_only=True,
        max_length=30,
        trim_whitespace=True
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        max_length=30,
    )

    def validate(self, attrs: dict[str, str]) -> dict[str, Any]:
        username = attrs.get('username')
        password = attrs.get('password')

        if not username or not password:
            raise serializers.ValidationError(
                {
                    "message": "Must include both username and password to log in"
                }
            )

        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )

        if not user:
            raise serializers.ValidationError(
                {
                    "message": "Incorrect username or password"
                }
            )

        if not user.is_active:
            raise serializers.ValidationError(
                {
                    "message": "User account is disabled"
                }
            )

        if user.is_deleted:
            raise serializers.ValidationError(
                {
                    "message": "User account is deleted"
                }
            )

        attrs['user'] = user
        return attrs


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password"},
        trim_whitespace=False,
    )
    re_password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password"},
        trim_whitespace=False,
    )
    email = serializers.EmailField(
        required=True,
        trim_whitespace=False,
    )

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "re_password",
            "first_name",
            "last_name",
            "birth_date",
            "gender",
        ]

    def validate_email(self, value: str) -> str:
        value = value.strip().lower()

        if not value:
            raise serializers.ValidationError("Email is required.")

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email already exists.")

        return value

    def validate_first_name(self, value: str | None) -> str | None:
        if value in (None, ""):
            return value

        value = value.strip()

        if not re.fullmatch(r"^[a-zA-Z]+(?:[-'][a-zA-Z]+)*$", value):
            raise serializers.ValidationError(
                "First name must contain only alphabet characters."
            )

        return value

    def validate_last_name(self, value: str | None) -> str | None:
        if value in (None, ""):
            return value

        value = value.strip()

        if not re.fullmatch(r"^[a-zA-Z]+(?:[-'][a-zA-Z]+)*$", value):
            raise serializers.ValidationError(
                "Last name must contain only alphabet characters."
            )

        return value

    def validate(self, attrs):
        password = attrs.get("password")
        re_password = attrs.pop("re_password", None)
        birth_date = attrs.get("birth_date")

        try:
            validate_password(password)
        except ValidationError as e:
            msg = str(e.messages[0])
            raise serializers.ValidationError(
                {"password": msg},
                code="authorization",
            )

        if password != re_password:
            raise serializers.ValidationError(
                {"re_password": "Passwords do not match."}
            )

        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = User.objects.create_user(
            password=password,
            is_staff=False,
            is_active=True,
            is_deleted=False,
            **validated_data,
        )

        return user

