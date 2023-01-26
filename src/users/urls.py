from django.contrib.auth import get_user_model
from django.urls import path
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from users.serializers import UserRegistrationSerializer

User = get_user_model()


class UserCreateApi(CreateAPIView):
    model = User
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer


urlpatterns = [
    path("", UserCreateApi.as_view()),
]
