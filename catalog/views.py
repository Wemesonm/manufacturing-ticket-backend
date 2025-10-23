from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Site, ProcessType, Line, MachineType, Workstation, FailureCategory, FailureType, SeverityLevel, SLAProfile
from .serializers import SiteSerializer, ProcessTypeSerializer, LineSerializer, MachineTypeSerializer, WorkstationSerializer, FailureCategorySerializer, FailureTypeSerializer, SeverityLevelSerializer, SLAProfileSerializer
from core.pagination import AppPagination


class ROBase(viewsets.ReadOnlyModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    pagination_class = AppPagination

class SiteViewSet(ROBase):
    queryset = Site.objects.all().order_by("name")
    serializer_class = SiteSerializer
    search_fields = ["name", "description"]
    ordering_fields = ["name", "id"]

class ProcessTypeViewSet(ROBase):
    queryset = ProcessType.objects.all().order_by("name")
    serializer_class = ProcessTypeSerializer
    search_fields = ["name", "description"]
    ordering_fields = ["name", "id"]

class LineViewSet(ROBase):
    queryset = Line.objects.select_related("site", "process_type").all().order_by("code")
    serializer_class = LineSerializer
    filterset_fields = ["site", "process_type", "active"]        # ?site=1&process_type=2
    search_fields = ["code", "name"]
    ordering_fields = ["code", "name", "id"]

class MachineTypeViewSet(ROBase):
    queryset = MachineType.objects.all().order_by("name")
    serializer_class = MachineTypeSerializer
    search_fields = ["name", "description"]
    ordering_fields = ["name", "id"]

class WorkstationViewSet(ROBase):
    queryset = Workstation.objects.select_related("line", "machine_type").all().order_by("code")
    serializer_class = WorkstationSerializer
    filterset_fields = ["line", "machine_type", "active"]        # ?line=3&machine_type=2
    search_fields = ["code", "name", "asset_tag"]
    ordering_fields = ["code", "name", "id"]

class FailureCategoryViewSet(ROBase):
    queryset = FailureCategory.objects.select_related("parent").all().order_by("name")
    serializer_class = FailureCategorySerializer
    filterset_fields = ["parent"]                                 # ?parent=<id> (subcats)
    search_fields = ["name", "description"]
    ordering_fields = ["name", "id"]

class FailureTypeViewSet(ROBase):
    queryset = FailureType.objects.select_related("category").all().order_by("name")
    serializer_class = FailureTypeSerializer
    filterset_fields = ["category"]                               # ?category=<id>
    search_fields = ["name", "code", "ipc_ref", "description"]
    ordering_fields = ["name", "code", "id"]

class SeverityLevelViewSet(ROBase):
    queryset = SeverityLevel.objects.all().order_by("order", "name")
    serializer_class = SeverityLevelSerializer
    search_fields = ["name", "description"]
    ordering_fields = ["order", "name", "id"]

class SLAProfileViewSet(ROBase):
    queryset = SLAProfile.objects.select_related("severity").all().order_by("severity__order")
    serializer_class = SLAProfileSerializer
    filterset_fields = ["severity", "active"]                     # ?severity=<id>&active=true
    ordering_fields = ["mtta_target_min", "mttr_target_min", "id"]