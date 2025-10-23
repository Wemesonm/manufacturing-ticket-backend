from django.urls import path
from .views import (
    TicketListCreateView, TicketDetailView,
    TicketAcceptView, TicketArrivedView, TicketWorkView,
    TicketResolveView, TicketCloseView
)

urlpatterns = [
    path("", TicketListCreateView.as_view(), name="ticket-list-create"),
    path("<int:pk>/", TicketDetailView.as_view(), name="ticket-detail"),
    path("<int:pk>/accept/", TicketAcceptView.as_view(), name="ticket-accept"),
    path("<int:pk>/arrived/", TicketArrivedView.as_view(), name="ticket-arrived"),
    path("<int:pk>/work/", TicketWorkView.as_view(), name="ticket-work"),
    path("<int:pk>/resolve/", TicketResolveView.as_view(), name="ticket-resolve"),
    path("<int:pk>/close/", TicketCloseView.as_view(), name="ticket-close"),
]
