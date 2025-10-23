from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
 
    def __str__(self): 
        return self.name


class ProcessType(models.Model):
    name = models.CharField(max_length=100, unique=True)  # SMT, PTH, CELL, TEST, ...
    description = models.TextField(blank=True)

    def __str__(self): 
        return self.name


class Line(models.Model):
    site = models.ForeignKey(Site, on_delete=models.PROTECT, related_name="lines")
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=120)
    process_type = models.ForeignKey(ProcessType, on_delete=models.SET_NULL, null=True, blank=True, related_name="lines")
    active = models.BooleanField(default=True)

    def __str__(self): 
        return f"{self.code} - {self.name}"


class MachineType(models.Model):
    name = models.CharField(max_length=100, unique=True)  # SPI, PNP, AOI, Reflow, etc.
    description = models.TextField(blank=True)

    def __str__(self): 
        return self.name


class Workstation(models.Model):
    line = models.ForeignKey(Line, on_delete=models.PROTECT, related_name="stations")
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=120)
    machine_type = models.ForeignKey(MachineType, on_delete=models.SET_NULL, null=True, blank=True, related_name="stations")
    asset_tag = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self): 
        return f"{self.code} - {self.name}"


class FailureCategory(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="subcategories")

    def __str__(self): 
        return self.name


class FailureType(models.Model):
    category = models.ForeignKey(FailureCategory, on_delete=models.PROTECT, related_name="failures")
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=50, blank=True)
    ipc_ref = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    def __str__(self): 
        return f"{self.code or ''} {self.name}".strip()


class SeverityLevel(models.Model):
    name = models.CharField(max_length=50, unique=True)  # ex.: S0, S1, Critical...
    description = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self): 
        return self.name


class SLAProfile(models.Model):
    severity = models.ForeignKey(SeverityLevel, on_delete=models.PROTECT, related_name="sla_rules")
    mtta_target_min = models.PositiveIntegerField(default=10)
    mttr_target_min = models.PositiveIntegerField(default=60)
    active = models.BooleanField(default=True)

    def __str__(self): 
        return f"{self.severity.name}: MTTA {self.mtta_target_min} / MTTR {self.mttr_target_min}"