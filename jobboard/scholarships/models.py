from django.db import models
from django.conf import settings

class ScholarshipPost(models.Model):
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="scholarship_posts")
    title = models.CharField(max_length=255)
    description = models.TextField()
    eligibility_criteria = models.TextField(blank=True)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
