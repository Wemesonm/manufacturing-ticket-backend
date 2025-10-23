from django.contrib import admin
from .models import Ticket, TicketStatus


admin.site.register(Ticket)
admin.site.register(TicketStatus)
