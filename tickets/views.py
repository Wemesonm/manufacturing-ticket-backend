from django.utils import timezone
from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from .models import Ticket
from .serializers import TicketSerializer, TicketUpdateSerializer
from .filters import TicketFilter

class IsAuthenticatedOrReadOnly(permissions.IsAuthenticated):
    """ajuste aqui se quiser liberar GET sem token"""
    pass

# ------ CRUD principal ------
class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.select_related(
        "line", "workstation", "failure_type__category", "severity",
        "opened_by", "assigned_to"
    ).all().order_by("-created_at")
    serializer_class = TicketSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = TicketFilter
    ordering_fields = ["created_at", "severity__order", "status"]
    search_fields = ["title", "description", "root_cause", "corrective_action"]

class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ("PUT", "PATCH"):
            return TicketUpdateSerializer
        return TicketSerializer

# ------ Ações de fluxo (POST) ------
class TicketAcceptView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        t = get_object_or_404(Ticket, pk=pk)
        # TODO: checar se user pode aceitar (ex.: suporte)
        t.mark_accepted(request.user)
        t.save()
        return Response(TicketSerializer(t).data, status=status.HTTP_200_OK)

class TicketArrivedView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        t = get_object_or_404(Ticket, pk=pk)
        # TODO: checar se user é líder da linha para confirmar chegada
        t.mark_arrived()
        t.save()
        return Response(TicketSerializer(t).data, status=status.HTTP_200_OK)

class TicketWorkView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        t = get_object_or_404(Ticket, pk=pk)
        # TODO: checar se assigned_to == request.user (ou suporte)
        t.mark_working()
        t.save()
        return Response(TicketSerializer(t).data, status=status.HTTP_200_OK)

class TicketResolveView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        t = get_object_or_404(Ticket, pk=pk)
        # TODO: checar se assigned_to == request.user (ou suporte)
        t.mark_resolved()
        t.save()
        return Response(TicketSerializer(t).data, status=status.HTTP_200_OK)

class TicketCloseView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        t = get_object_or_404(Ticket, pk=pk)
        # TODO: checar se user é líder da linha
        t.mark_closed()
        t.save()
        return Response(TicketSerializer(t).data, status=status.HTTP_200_OK)