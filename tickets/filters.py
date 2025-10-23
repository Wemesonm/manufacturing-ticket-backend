import django_filters
from .models import Ticket

class TicketFilter(django_filters.FilterSet):
    created_from = django_filters.DateTimeFilter(field_name="created_at", lookup_expr="gte")
    created_to = django_filters.DateTimeFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = Ticket
        fields = {
            "line": ["exact"],
            "workstation": ["exact"],
            "failure_type": ["exact"],
            "severity": ["exact"],
            "status": ["exact"],
            "opened_by": ["exact"],
            "assigned_to": ["exact", "isnull"],
        }
