from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("exchange-rates/", include("exchange_rates.urls")),
    path("", include("core.urls")),
    path("users/", include("users.urls")),
    path("auth/", include("authentication.urls")),
    path("static/<path:path>/", serve, {"document_root": settings.STATIC_ROOT}),
]
