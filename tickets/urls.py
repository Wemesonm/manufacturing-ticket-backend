from django.urls import path
from .views import TicketListCreateView, TicketRetriveUpdateDestroyView

urlpatterns = [
    path("", TicketListCreateView.as_view(), name="ticket-list-create"),
    path("<int:pk>/", TicketRetriveUpdateDestroyView.as_view(), name="ticket-detail-view"),
]
