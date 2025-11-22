from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Ticket, TicketStatus
from .serializers import TicketModelSerializer, TicketListDetailSerializer, TicketStatusSerializer
from core.pagination import AppPagination
from core.permissions import GlobalDefaultPermission


class TicketListCreateView(generics.ListCreateAPIView):
    permission_classes =(IsAuthenticated, GlobalDefaultPermission,)
    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer
    pagination_class = AppPagination
    
    def perform_create(self, serializer):
        serializer.save(opened_by=self.request.user)


class TicketRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes =(IsAuthenticated, GlobalDefaultPermission,)
    queryset = Ticket.objects.all()
    serializer_class = TicketListDetailSerializer
    pagination_class = AppPagination


class TicketStatusListView(generics.ListAPIView):
    permission_classes =(IsAuthenticated,)
    queryset = TicketStatus.objects.all()
    serializer_class = TicketStatusSerializer
    pagination_class = AppPagination

class TicketStatusDetailView(generics.RetrieveAPIView):
    permission_classes =(IsAuthenticated,)
    queryset = TicketStatus.objects.all()
    serializer_class = TicketStatusSerializer