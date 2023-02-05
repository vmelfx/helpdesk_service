from django.http import JsonResponse
from rest_framework import status
from rest_framework.viewsets import ViewSet
from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from users.models import User
from users.serializers import (
    UserListSerializer,
    UserRegistrationSerializer,
    UserRetrieveSerializer,
)


class UsersAPISet(ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserListSerializer(queryset, many=True)

        response = ResponseMultiSerializer({"results": serializer.data})

        return JsonResponse(response.data)

    def retrieve(self, request, pk: int):
        queryset = User.objects.get(id=pk)
        serializer = UserRetrieveSerializer(queryset)

        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def create(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk: int):
        context: dict = {
            "request": self.request,
        }
        instance = User.objects.get(id=pk)
        serializer = UserRegistrationSerializer(instance, data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def destroy(self, request, pk: int):
        User.objects.get(id=pk).delete()

        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
