from rest_framework import generics, permissions, filters
from .models import Application
from .serializers import ApplicationSerializer

class MyApplicationsList(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user).order_by("-applied_at")

class ApplicationCreate(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

class ManageApplicationsList(generics.ListAPIView):
    """For company/org users to see applications for their postings."""
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Applications to jobs posted_by user OR scholarships posted_by user
        return Application.objects.filter(
            models.Q(job__posted_by=user) | models.Q(scholarship__posted_by=user)
        ).order_by("-applied_at")
