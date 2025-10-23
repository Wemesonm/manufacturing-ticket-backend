from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SiteViewSet, ProcessTypeViewSet, LineViewSet, MachineTypeViewSet, WorkstationViewSet, FailureCategoryViewSet, FailureTypeViewSet, SeverityLevelViewSet, SLAProfileViewSet


router = DefaultRouter()
router.register(r"sites", SiteViewSet, basename="site")
router.register(r"process-types", ProcessTypeViewSet, basename="processtype")
router.register(r"lines", LineViewSet, basename="line")
router.register(r"machine-types", MachineTypeViewSet, basename="machinetype")
router.register(r"stations", WorkstationViewSet, basename="workstation")
router.register(r"failure-categories", FailureCategoryViewSet, basename="failurecategory")
router.register(r"failure-types", FailureTypeViewSet, basename="failuretype")
router.register(r"severities", SeverityLevelViewSet, basename="severitylevel")
router.register(r"sla-profiles", SLAProfileViewSet, basename="slaprofile")

urlpatterns = [path("", include(router.urls))]