from django.contrib import admin
from tickets.models import Ticket
from shared.django import TimeStampReadonlyAdmin


@admin.register(Ticket)
class TicketsAdmin(TimeStampReadonlyAdmin):
    pass
