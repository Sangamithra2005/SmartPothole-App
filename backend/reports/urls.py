from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PotholeReportViewSet

router = DefaultRouter()
router.register(r'reports', PotholeReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
