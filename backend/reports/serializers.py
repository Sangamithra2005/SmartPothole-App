from rest_framework import serializers
from .models import PotholeReport

class PotholeReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PotholeReport
        fields = '__all__'
