from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {"password": {"write_only": True}}
        fields = ["email", "password"]
