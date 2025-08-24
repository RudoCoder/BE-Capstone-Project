from rest_framework import viewsets, permissions, filters
from .models import JobPost
from .serializers import JobPostSerializer
from .permissions import IsCompanyOrReadOnly, IsOwnerOrReadOnly

class JobPostViewSet(viewsets.ModelViewSet):
    queryset = JobPost.objects.all().order_by("-created_at")
    serializer_class = JobPostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "description", "location"]

    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            return [permissions.AllowAny()]
        return [IsCompanyOrReadOnly(), IsOwnerOrReadOnly()]
