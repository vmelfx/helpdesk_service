from django.urls import path
from tickets.api import ticket_create, ticket_retrieve, ticket_update, tickets_list

urlpatterns = [
    path("", ticket_create),
    path("", tickets_list),
    path("", ticket_update),
    path("<int:id_>/", ticket_retrieve),
]
