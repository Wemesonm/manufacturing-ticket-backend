from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from core.utils import minutes_between
from catalog.models import Line, Workstation, FailureType, SeverityLevel

User = get_user_model()


class TicketStatus(models.Model):
    """
    Cadastro de status do fluxo do ticket.
    Exemplo:
      Open → Accepted → On Site → Working → Resolved → Closed
    """
    code = models.CharField(max_length=40, unique=True)  # identificador interno (ex: OPEN)
    name = models.CharField(max_length=80)               # nome visível (ex: "Open")
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)       # ordem no fluxo
    is_final = models.BooleanField(default=False)
    color = models.CharField(max_length=20, blank=True)  # opcional para UI
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.name}"


class Ticket(models.Model):
    """
    Registro de chamados abertos no chão de fábrica.
    """
    # relacionamento com catálogo
    line = models.ForeignKey(Line, on_delete=models.PROTECT, related_name="tickets")
    workstation = models.ForeignKey(Workstation, on_delete=models.PROTECT, null=True, blank=True, related_name="tickets")
    failure_type = models.ForeignKey(FailureType, on_delete=models.PROTECT, null=True, blank=True, related_name="tickets")
    severity = models.ForeignKey(SeverityLevel, on_delete=models.PROTECT, related_name="tickets")

    # status dinâmico
    status = models.ForeignKey(TicketStatus, on_delete=models.PROTECT, related_name="tickets")

    # dados básicos
    title = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    hold_line = models.BooleanField(default=False)

    # usuários
    opened_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="opened_tickets")
    assigned_to = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name="assigned_tickets")

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    accepted_at = models.DateTimeField(null=True, blank=True)
    on_site_at = models.DateTimeField(null=True, blank=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    # RCA
    root_cause = models.CharField(max_length=140, blank=True)
    containment = models.TextField(blank=True)
    corrective_action = models.TextField(blank=True)
    preventive_action = models.TextField(blank=True)

    # métricas calculadas
    @property
    def mtta_minutes(self):
        return minutes_between(self.created_at, self.on_site_at)

    @property
    def mttr_minutes(self):
        return minutes_between(self.created_at, self.closed_at)

    def __str__(self):
        return f"[{self.status.name}] {self.title}"