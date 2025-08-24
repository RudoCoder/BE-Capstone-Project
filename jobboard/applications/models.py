from django.db import models
from django.conf import settings
from django.db.models import Q

class Application(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="applications")
    job = models.ForeignKey("jobs.JobPost", on_delete=models.CASCADE, null=True, blank=True, related_name="applications")
    scholarship = models.ForeignKey("scholarships.ScholarshipPost", on_delete=models.CASCADE, null=True, blank=True, related_name="applications")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=(
                    (Q(job__isnull=False) & Q(scholarship__isnull=True)) |
                    (Q(job__isnull=True) & Q(scholarship__isnull=False))
                ),
                name="application_exactly_one_target",
            )
        ]

    def __str__(self):
        target = self.job or self.scholarship
        return f"{self.user.username} -> {target}"
