# core/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "authentication": {
            "token_obtain_pair": reverse("token_obtain_pair", request=request),
            "token_refresh": reverse("token_refresh", request=request),
            "token_verify": reverse("token_verify", request=request),
        },

        "catalog": {
            "sites": reverse("catalog:site-list", request=request),
            "lines": reverse("catalog:line-list", request=request),
            "workstations": reverse("catalog:workstation-list", request=request),
            "failure_categories": reverse("catalog:failurecategory-list", request=request),
            "failure_types": reverse("catalog:failuretype-list", request=request),
            "severities": reverse("catalog:severitylevel-list", request=request),
            "sla_profiles": reverse("catalog:slaprofile-list", request=request),
        },

        "tickets": {
            "tickets": reverse("ticket-list-create", request=request),
            "ticket_status": reverse("ticketstatus-list", request=request),
        },
    })


urlpatterns = [
    path('ticketapi/admin/', admin.site.urls),

    # Root da API
    path('ticketapi/v1/', api_root, name="api-root"),

    # Apps
    path('ticketapi/v1/', include('authentication.urls')),
    path('ticketapi/v1/', include("catalog.urls")),
    path('ticketapi/v1/', include("tickets.urls")),
]



# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/', include('authentication.urls')),
#     path('api/v1/', include("catalog.urls")),
#     path('api/v1/', include("tickets.urls")),
# ]
