from django.urls import path
from .views import TicketListCreateView, TicketRetriveUpdateDestroyView, TicketStatusListView, TicketStatusDetailView

urlpatterns = [
    path("tickets/", TicketListCreateView.as_view(), name="ticket-list-create"),
    path("tickets/<int:pk>/", TicketRetriveUpdateDestroyView.as_view(), name="ticket-detail-view"),
    path("ticket-status/", TicketStatusListView.as_view(), name="ticketstatus-list"),
    path("ticket-status/<int:pk>/", TicketStatusDetailView.as_view(), name="ticketstatus-detail"),
]
