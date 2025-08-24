from rest_framework import serializers
from .models import JobPost

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = ["id", "title", "description", "requirements", "location", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]

    def create(self, validated_data):
        user = self.context["request"].user
        return JobPost.objects.create(posted_by=user, **validated_data)
