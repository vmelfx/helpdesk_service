from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from tickets.models import Ticket
from tickets.serializers import TicketLightSerializer, TicketSerializer


class TicketApiSet(ViewSet):
    def list(self, request):
        queryset = Ticket.objects.all()
        serializer = TicketLightSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})

        return Response(response.data)

    def retrieve(self, request, pk: int):
        instance = Ticket.objects.get(id=pk)
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
        instance = Ticket.objects.get(id=pk)

        context: dict = {
            "request": self.request,
        }
        serializer = TicketSerializer(instance, data=request.data, context=context)
        serializer.is_valid()
        serializer.save()

        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def destroy(self, request, pk: int):
        Ticket.objects.get(id=pk).delete()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
