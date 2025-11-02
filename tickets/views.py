from rest_framework import generics
from .models import Ticket
from .serializers import TicketModelSerializer, TicketListDetailSerializer
from core.pagination import AppPagination


class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer
    pagination_class = AppPagination


class TicketRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketListDetailSerializer
    pagination_class = AppPagination