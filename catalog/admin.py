from django.contrib import admin
from .models import (
    Site, ProcessType, Line, MachineType, Workstation,
    FailureCategory, FailureType, SeverityLevel, SLAProfile
)

admin.site.register([
  Site,
  ProcessType,
  Line,
  MachineType,
  Workstation,
  FailureCategory,
  FailureType,
  SeverityLevel,
  SLAProfile
  ])