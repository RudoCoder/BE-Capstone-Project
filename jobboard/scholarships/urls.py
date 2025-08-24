from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScholarshipPostViewSet

router = DefaultRouter()
router.register(r"scholarships", ScholarshipPostViewSet, basename="scholarships")

urlpatterns = [path("", include(router.urls))]
