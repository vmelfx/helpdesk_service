from django.urls import include, path

urlpatterns = [
    path("tickets/", include("tickets.urls")),
    path("users/", include("users.urls")),
    path("tickets/<int:ticket_id>/comments/", include("comments.urls")),
    path("tickets/<int:ticket_id>/comments/create/", include("comments.urls")),
]
