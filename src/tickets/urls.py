# from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.urls import path
from django.views.generic import ListView
from tickets.models import Ticket


def tickets_get(request):
    # tickets: QuerySet = Ticket.objects.all()
    return JsonResponse({})


class TicketsGet(ListView):
    model = Ticket


urlpatterns = [
    path("", TicketsGet.as_view()),
]
