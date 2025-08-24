from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["id", "user", "job", "scholarship", "status", "applied_at"]
        read_only_fields = ["user", "status", "applied_at"]

    def validate(self, data):
        job = data.get("job")
        scholarship = data.get("scholarship")
        if bool(job) == bool(scholarship):
            raise serializers.ValidationError("Provide exactly one of job or scholarship.")
        return data

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
