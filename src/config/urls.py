from django.contrib import admin
from django.urls import include, path
import json
from dataclasses import asdict, dataclass

from django.http import HttpResponse


@dataclass
class Person:
    name: str
    age: int


def signup(variable):
    john = Person(name="John", age=30)
    content = json.dumps(asdict(john))
    content_type = "application/json"
    return HttpResponse(content, content_type=content_type)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("exchange-rates/", include("exchange_rates.urls")),
    path("signup/", signup),
]
