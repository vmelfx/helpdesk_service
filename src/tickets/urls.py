from django.urls import  path
from django.http import JsonResponse


def tickets_get(request):
    return JsonResponse({"tickets": []})


urlpatterns = [
    path("", tickets_get),
]
