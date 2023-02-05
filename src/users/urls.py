from rest_framework.routers import DefaultRouter
from users.api import UsersAPISet

router = DefaultRouter()
router.register("", UsersAPISet, basename="")
urlpatterns = router.urls
