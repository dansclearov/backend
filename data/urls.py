from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)

router.register(prefix="data", viewset=views.BinsViewSet, basename="data")
router.register(prefix="dashboard/bin-activity", viewset=views.DashboardBinViewSet, basename="dashboard/bin-activity")
router.register(prefix="dashboard/general-statistics", viewset=views.DashboardBinGeneralStatsViewSet,
                basename="dashboard/general-statistics")
router.register(prefix="dashboard/diesel-consumption", viewset=views.DashboardDieselViewSet,
                basename="dashboard/diesel-consumption")
router.register(prefix="bins", viewset=views.DashboardBinsViewSet, basename="bins")
router.register(prefix="dashboard/co2-emissions", viewset=views.DashboardCo2ViewSet, basename="dashboard/co2-emissions")

urlpatterns = [] + router.urls
