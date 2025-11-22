from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Site, Line, Workstation, FailureCategory, FailureType, SeverityLevel, SLAProfile
from .serializers import *
from core.pagination import AppPagination
from core.permissions import GlobalDefaultPermission
class ROBaseList(generics.ListAPIView):
    permission_classes =(IsAuthenticated,GlobalDefaultPermission,)
    pagination_class = AppPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    # subclasses definem: queryset, serializer_class, filterset_fields, search_fields, ordering_fields

class ROBaseDetail(generics.RetrieveAPIView):
    # subclasses definem: queryset, serializer_class
     permission_classes =(IsAuthenticated, GlobalDefaultPermission,)
class SiteList(ROBaseList):
    queryset = Site.objects.all().order_by("name")
    serializer_class = SiteSerializer
    search_fields = ["name", "description"]
    ordering_fields = ["name", "id"]

class SiteDetail(ROBaseDetail):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class LineList(ROBaseList):
    queryset = Line.objects.select_related("site").all().order_by("code")
    serializer_class = LineSerializer
    filterset_fields = ["site", "active"]
    search_fields = ["code", "name"]
    ordering_fields = ["code", "name", "id"]

class LineDetail(ROBaseDetail):
    queryset = Line.objects.all()
    serializer_class = LineSerializer

class WorkstationList(ROBaseList):
    queryset = Workstation.objects.select_related("line").all().order_by("order")
    serializer_class = WorkstationSerializer
    filterset_fields = ["line", "active"]
    search_fields = ["code", "name", "asset_tag"]
    ordering_fields = ["order", "name", "id"]

class WorkstationDetail(ROBaseDetail):
    queryset = Workstation.objects.all()
    serializer_class = WorkstationSerializer

class FailureCategoryList(ROBaseList):
    queryset = FailureCategory.objects.all().order_by("name")
    serializer_class = FailureCategorySerializer
    search_fields = ["name", "code", "description"]
    ordering_fields = ["name", "id"]

class FailureCategoryDetail(ROBaseDetail):
    queryset = FailureCategory.objects.all()
    serializer_class = FailureCategorySerializer

class FailureTypeList(ROBaseList):
    queryset = FailureType.objects.select_related("category").all().order_by("name")
    serializer_class = FailureTypeSerializer
    filterset_fields = ["category"]
    search_fields = ["name", "code", "description"]
    ordering_fields = ["name", "code", "id"]

class FailureTypeDetail(ROBaseDetail):
    queryset = FailureType.objects.all()
    serializer_class = FailureTypeSerializer

class SeverityLevelList(ROBaseList):
    queryset = SeverityLevel.objects.all().order_by("order", "name")
    serializer_class = SeverityLevelSerializer
    search_fields = ["name", "description"]
    ordering_fields = ["order", "name", "id"]

class SeverityLevelDetail(ROBaseDetail):
    queryset = SeverityLevel.objects.all()
    serializer_class = SeverityLevelSerializer

class SLAProfileList(ROBaseList):
    queryset = SLAProfile.objects.select_related("severity").all().order_by("severity__order")
    serializer_class = SLAProfileSerializer
    filterset_fields = ["severity", "active"]
    ordering_fields = ["mtta_target_min", "mttr_target_min", "id"]

class SLAProfileDetail(ROBaseDetail):
    queryset = SLAProfile.objects.all()
    serializer_class = SLAProfileSerializer