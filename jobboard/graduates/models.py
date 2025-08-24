from django.db import models
from django.conf import settings

class GraduateProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    university = models.CharField(max_length=255, blank=True)
    degree = models.CharField(max_length=255, blank=True)
    skills = models.TextField(blank=True)  # could be JSON in future
    cv_file = models.URLField(blank=True)  # URL for simplicity

    def __str__(self):
        return f"{self.user.username} Profile"
