# tickets/serializers.py
from rest_framework import serializers
from .models import Ticket, TicketStatus

class TicketModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = "__all__"
        read_only_fields = ["opened_by"]
        

class TicketListDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ticket
        fields = "__all__"
        read_only_fields = ["opened_by"]


class TicketStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketStatus
        fields = "__all__"
