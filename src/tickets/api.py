from django.http import JsonResponse
from rest_framework import status
from rest_framework.viewsets import ViewSet
from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from tickets.models import Ticket
from tickets.serializers import TicketLightSerializer, TicketSerializer


class TicketApiSet(ViewSet):
    def list(self, request):
        queryset = Ticket.objects.all()
        serializer = TicketLightSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})
        return JsonResponse(response.data)

    def retrieve(self, request, id_: int):
        instance = Ticket.objects.get(id=id_)
        serializer = TicketSerializer(instance)
        response = ResponseSerializer({"result": serializer.data})
        return JsonResponse(response.data)

    def create(self, request, id_=None):
        context: dict = {
            "request": self.request,
        }
        serializer = TicketSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})
        return JsonResponse(response.data, status=status.HTTP_201_CREATED)


tickets_list = TicketApiSet.as_view({"get": "list"})
ticket_retrieve = TicketApiSet.as_view({"get": "retrieve"})
ticket_create = TicketApiSet.as_view({"post": "create"})
ticket_update = TicketApiSet.as_view({"put": "update"})
