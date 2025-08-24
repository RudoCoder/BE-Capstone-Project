from rest_framework import serializers
from .models import GraduateProfile

class GraduateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraduateProfile
        fields = ["id", "university", "degree", "skills", "cv_file"]
