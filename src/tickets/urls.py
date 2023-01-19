from django.urls import path
from django.http import JsonResponse
import sqlite3
from dataclasses import dataclass, asdict
from typing import Iterable, Any


@dataclass()
class Ticket:
    id: int
    created_at: str
    updated_at: str
    header: str
    body: str
    customer_id: str
    manager_id: str


def _tickets_get(request):
    connection: sqlite3.Connection = sqlite3.connect("db.sqlite3")
    cursor: sqlite3.Cursor = connection.cursor()
    data: Iterable = cursor.execute("SELECT * FROM tickets_ticket")

    field_names: list[str] = [el[0] for el in cursor.description]
    tickets: list[Ticket] = []

    for result in data:
        payload: dict[str, Any] = {}
        for field_name, value in zip(field_names, result):
            payload[field_name] = value
        tickets.append(Ticket(**payload))

    tickets_dicts: list[dict] = [asdict(ticket) for ticket in tickets]
    return JsonResponse({"tickets": tickets_dicts})


urlpatterns = [
    path("", tickets_get),
]
