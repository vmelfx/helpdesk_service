from django.contrib.auth import get_user_model
from django.urls import path
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from users.serializers import UserRegistrationSerializer

User = get_user_model()


class UserCreateApi(CreateAPIView):
    model = User
    permission_classes = permissions.AllowAny
    serializer_class = UserRegistrationSerializer


urlpatterns = [
    path("", UserCreateApi.as_view()),
]
