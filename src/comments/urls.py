from comments.api import CommentsAPISet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", CommentsAPISet, basename="")
urlpatterns = router.urls


# In this application we didn't follow the HTTP approach
# to have two different approaches in this project

# urlpatterns = [
#     path("<int:ticket_id>/comments",
#          CommentsListAPI.as_view()),
# ]
