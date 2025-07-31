from rest_framework import viewsets
from .models import PotholeReport
from .serializers import PotholeReportSerializer

class PotholeReportViewSet(viewsets.ModelViewSet):
    queryset = PotholeReport.objects.all()
    serializer_class = PotholeReportSerializer
