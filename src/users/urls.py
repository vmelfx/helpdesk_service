from django.contrib.auth import get_user_model
from django.urls import path
from rest_framework.generics import CreateAPIView
from users.serializers import UserRegistrationSerializer

User = get_user_model()


class UserCreateApi(CreateAPIView):
    serializer_class = UserRegistrationSerializer


urlpatterns = [
    path("", UserCreateApi.as_view()),
]
