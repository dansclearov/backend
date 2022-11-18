from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)

router.register(prefix="data", viewset=views.BinsViewSet, basename="data")

urlpatterns = [] + router.urls
