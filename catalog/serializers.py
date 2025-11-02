from rest_framework import serializers
from .models import Site, Line, Workstation,FailureCategory, FailureType, SeverityLevel, SLAProfile

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model =Site;
        fields = "__all__"

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model =Line;
        fields = "__all__"

class WorkstationSerializer(serializers.ModelSerializer):
    class Meta:
        model =Workstation;
        fields = "__all__"

class FailureCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =FailureCategory;
        fields = "__all__"

class FailureTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model =FailureType;
        fields = "__all__"

class SeverityLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model =SeverityLevel;
        fields = "__all__"

class SLAProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =SLAProfile;
        fields = "__all__"
