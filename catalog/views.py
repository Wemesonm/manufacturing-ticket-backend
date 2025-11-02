from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Site, Line, Workstation, FailureCategory, FailureType, SeverityLevel, SLAProfile
from .serializers import (
    SiteSerializer, LineSerializer, WorkstationSerializer,
    FailureCategorySerializer, FailureTypeSerializer,
    SeverityLevelSerializer, SLAProfileSerializer
)
from core.pagination import AppPagination

class ROBase(viewsets.ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    pagination_class = AppPagination

class SiteViewSet(ROBase):
    queryset = Site.objects.all().order_by("name")
    serializer_class = SiteSerializer
    search_fields = ["name", "description"]
    ordering_fields = ["name", "id"]

class LineViewSet(ROBase):
    queryset = Line.objects.select_related("site").all().order_by("code")
    serializer_class = LineSerializer
    filterset_fields = ["site", "active"]
    search_fields = ["code", "name"]
    ordering_fields = ["code", "name", "id"]

class WorkstationViewSet(ROBase):
    queryset = Workstation.objects.select_related("line").all().order_by("code")
    serializer_class = WorkstationSerializer
    filterset_fields = ["line", "active"]
    search_fields = ["code", "name", "asset_tag"]
    ordering_fields = ["code", "name", "id"]

class FailureCategoryViewSet(ROBase):
    queryset = FailureCategory.objects.all().order_by("name")
    serializer_class = FailureCategorySerializer
    filterset_fields = []
    search_fields = ["name", "code", "description"]
    ordering_fields = ["name", "id"]

class FailureTypeViewSet(ROBase):
    queryset = FailureType.objects.select_related("category").all().order_by("name")
    serializer_class = FailureTypeSerializer
    filterset_fields = ["category"]
    search_fields = ["name", "code", "description"]
    ordering_fields = ["name", "code", "id"]

class SeverityLevelViewSet(ROBase):
    queryset = SeverityLevel.objects.all().order_by("order", "name")
    serializer_class = SeverityLevelSerializer
    search_fields = ["name", "description"]
    ordering_fields = ["order", "name", "id"]

class SLAProfileViewSet(ROBase):
    queryset = SLAProfile.objects.select_related("severity").all().order_by("severity__order")
    serializer_class = SLAProfileSerializer
    filterset_fields = ["severity", "active"]
    ordering_fields = ["mtta_target_min", "mttr_target_min", "id"]
