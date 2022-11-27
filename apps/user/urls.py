from rest_framework import routers

from apps.user.views import UserViewSet

app_name = "user"

router = routers.SimpleRouter()

router.register(r"", UserViewSet, basename="user")

urlpatterns = [] + router.urls
