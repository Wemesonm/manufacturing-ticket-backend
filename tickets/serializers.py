# tickets/serializers.py
from rest_framework import serializers
from .models import Ticket, TicketStatus


class TicketSerializer(serializers.ModelSerializer):
    # leitura (read-only)
    mtta_minutes = serializers.ReadOnlyField()
    mttr_minutes = serializers.ReadOnlyField()
    opened_by_username = serializers.CharField(source="opened_by.username", read_only=True)
    assigned_to_username = serializers.CharField(source="assigned_to.username", read_only=True)
    status_code = serializers.CharField(source="status.code", read_only=True)
    status_name = serializers.CharField(source="status.name", read_only=True)

    # escrita (write-able) — aceita status por PK, mas é opcional
    status = serializers.PrimaryKeyRelatedField(
        queryset=TicketStatus.objects.all(),
        required=False,
        help_text="ID do status (opcional no create; se ausente vira OPEN)."
    )

    class Meta:
        model = Ticket
        fields = "__all__"
        read_only_fields = (
            "accepted_at", "on_site_at", "resolved_at", "closed_at",
            "opened_by", "mtta_minutes", "mttr_minutes",
            # status NÃO está read-only aqui para permitir enviar no POST, se quiser
        )

    def create(self, validated_data):
        # opened_by = request.user
        request = self.context.get("request")
        if request and request.user and request.user.is_authenticated:
            validated_data["opened_by"] = request.user

        # define status OPEN se não informado
        if "status" not in validated_data or validated_data["status"] is None:
            try:
                validated_data["status"] = TicketStatus.objects.get(code="OPEN")
            except TicketStatus.DoesNotExist:
                raise serializers.ValidationError(
                    {"status": "Status 'OPEN' não encontrado. Carregue o ticket_status_seed.json."}
                )
        return super().create(validated_data)


class TicketUpdateSerializer(serializers.ModelSerializer):
    """PATCH/PUT durante o fluxo. Permite mudar status e demais campos editáveis."""
    status = serializers.PrimaryKeyRelatedField(
        queryset=TicketStatus.objects.all(), required=False
    )

    class Meta:
        model = Ticket
        fields = (
            "title", "description", "line", "workstation", "failure_type",
            "severity", "hold_line", "assigned_to", "status",
            "root_cause", "containment", "corrective_action", "preventive_action",
        )