from rest_framework import serializers
from .models import Site, ProcessType, Line, MachineType, Workstation,FailureCategory, FailureType, SeverityLevel, SLAProfile

class SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model =Site;
        fields = "__all__"

class ProcessTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model =Site;
        fields = "__all__"

class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model =Site;
        fields = "__all__"

class MachineTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model =Site;
        fields = "__all__"

class WorkstationSerializer(serializers.ModelSerializer):

    class Meta:
        model =Site;
        fields = "__all__"

class FailureCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model =Site;
        fields = "__all__"

class FailureTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model =Site;
        fields = "__all__"

class SeverityLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model =Site;
        fields = "__all__"

class SLAProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model =Site;
        fields = "__all__"
