from django.urls import path
from users.api import UserCreateApi

urlpatterns = [
    path("", UserCreateApi.as_view()),
]
