from django.contrib import admin
from .models import (
    Site, Line, Workstation,
    FailureCategory, FailureType, SeverityLevel, SLAProfile
)

admin.site.register([
  Site,
  Line,
  FailureCategory,
  FailureType,
  SLAProfile
  ])

@admin.register(Workstation)
class Workstation(admin.ModelAdmin):
    list_display = ("order", "name")
    list_filter = ("line",)
    search_fields = ("line", "name", "order",)
    ordering = ("order",)

@admin.register(SeverityLevel)
class SeverityLevel(admin.ModelAdmin):
    list_display = ("order", "name")
    ordering = ("order",)