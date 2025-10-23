# core/utils.py
from django.utils import timezone

def minutes_between(start, end):
    """
    Retorna a diferença em minutos entre dois datetimes.
    Se algum for None, retorna None. Converte para aware se necessário.
    """
    if not start or not end:
        return None

    # Garante que ambos sejam timezone-aware
    if timezone.is_naive(start):
        start = timezone.make_aware(start, timezone.get_current_timezone())
    if timezone.is_naive(end):
        end = timezone.make_aware(end, timezone.get_current_timezone())

    delta = end - start
    return int(delta.total_seconds() // 60)
