from django.urls import path
from .views import *

app_name = "catalog"

urlpatterns = [
    path("sites/", SiteList.as_view(), name="site-list"),
    path("sites/<int:pk>/", SiteDetail.as_view(), name="site-detail"),

    path("lines/", LineList.as_view(), name="line-list"),
    path("lines/<int:pk>/", LineDetail.as_view(), name="line-detail"),

    path("workstations/", WorkstationList.as_view(), name="workstation-list"),
    path("workstations/<int:pk>/", WorkstationDetail.as_view(), name="workstation-detail"),

    path("failure-categories/", FailureCategoryList.as_view(), name="failurecategory-list"),
    path("failure-categories/<int:pk>/", FailureCategoryDetail.as_view(), name="failurecategory-detail"),

    path("failure-types/", FailureTypeList.as_view(), name="failuretype-list"),
    path("failure-types/<int:pk>/", FailureTypeDetail.as_view(), name="failuretype-detail"),

    path("severities/", SeverityLevelList.as_view(), name="severitylevel-list"),
    path("severities/<int:pk>/", SeverityLevelDetail.as_view(), name="severitylevel-detail"),

    path("sla-profiles/", SLAProfileList.as_view(), name="slaprofile-list"),
    path("sla-profiles/<int:pk>/", SLAProfileDetail.as_view(), name="slaprofile-detail"),
]