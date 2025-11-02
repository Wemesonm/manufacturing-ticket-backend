# tickets/serializers.py
from rest_framework import serializers
from .models import Ticket, TicketStatus

class TicketModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = "__all__"
        

class TicketListDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ticket
        fields = "__all__"
