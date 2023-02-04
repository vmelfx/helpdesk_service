from rest_framework.routers import DefaultRouter
from tickets.api import TicketApiSet

router = DefaultRouter()
router.register("", TicketApiSet, basename="")
urlpatterns = router.urls
