from rest_framework import generics, permissions
from .models import GraduateProfile
from .serializers import GraduateProfileSerializer

class MyProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = GraduateProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        profile, _ = GraduateProfile.objects.get_or_create(user=self.request.user)
        return profile
