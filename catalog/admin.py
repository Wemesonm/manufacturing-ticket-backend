from django.contrib import admin
from .models import (
    Site, Line, Workstation,
    FailureCategory, FailureType, SeverityLevel, SLAProfile
)

admin.site.register([
  Site,
  Line,
  Workstation,
  FailureCategory,
  FailureType,
  SeverityLevel,
  SLAProfile
  ])