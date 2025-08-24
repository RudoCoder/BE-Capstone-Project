from rest_framework import serializers
from .models import ScholarshipPost

class ScholarshipPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipPost
        fields = ["id", "title", "description", "eligibility_criteria", "deadline", "created_at"]
        read_only_fields = ["created_at"]

    def create(self, validated_data):
        user = self.context["request"].user
        return ScholarshipPost.objects.create(posted_by=user, **validated_data)
