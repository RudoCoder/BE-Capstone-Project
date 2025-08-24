from rest_framework import viewsets, permissions, filters
from .models import ScholarshipPost
from .serializers import ScholarshipPostSerializer
from .permissions import IsOrgOrReadOnly, IsOwnerOrReadOnly

class ScholarshipPostViewSet(viewsets.ModelViewSet):
    queryset = ScholarshipPost.objects.all().order_by("-created_at")
    serializer_class = ScholarshipPostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "description"]

    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            return [permissions.AllowAny()]
        return [IsOrgOrReadOnly(), IsOwnerOrReadOnly()]
