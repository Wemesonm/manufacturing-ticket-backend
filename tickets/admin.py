from django.contrib import admin
from .models import Ticket, TicketStatus

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ticket._meta.fields]
    list_filter = ("line", "failure_type", "severity",)
    search_fields = ("line", "failure_type", "severity",)
    ordering = ("id",)


@admin.register(TicketStatus)
class TicketStatus(admin.ModelAdmin):
    list_display = [field.name for field in TicketStatus._meta.fields]
