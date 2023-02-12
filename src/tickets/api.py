from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet
from shared.permissions import PermissionsMixin
from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from tickets.models import Ticket
from tickets.permissions import IsOwner, RoleIsAdmin, RoleIsManager, RoleIsUser
from tickets.serializers import TicketLightSerializer, TicketSerializer


class TicketAPISet(ViewSet, GenericViewSet, PermissionsMixin):
    queryset = Ticket.objects.all()

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [RoleIsAdmin | RoleIsManager | RoleIsUser]
        elif self.action == "create":
            permission_classes = [RoleIsUser]
        elif self.action == "retrieve":
            permission_classes = [IsOwner | RoleIsAdmin | RoleIsManager]
        elif self.action == "update":
            permission_classes = [RoleIsUser | RoleIsManager | RoleIsAdmin]
        elif self.action == "destroy":
            permission_classes = [RoleIsAdmin | RoleIsManager]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def list(self, request):
        queryset = self._get_tickets()
        serializer = TicketLightSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})

        return Response(response.data)

    def retrieve(self, request, pk: int):
        instance: Ticket = self.get_object()
        serializer = TicketSerializer(instance)
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def create(self, request):
        context: dict = {
            "request": self.request,
        }
        serializer = TicketSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk: int):
        instance: Ticket = self.get_object()

        context: dict = {
            "request": self.request,
        }
        serializer = TicketSerializer(instance, data=request.data, context=context)
        serializer.is_valid()
        serializer.save()

        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def destroy(self, request, pk: int):
        instance: Ticket = self.get_object()
        instance.delete()

        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
