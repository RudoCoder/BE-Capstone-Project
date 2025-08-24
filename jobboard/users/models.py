from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Roles(models.TextChoices):
        GRADUATE = "graduate", "Graduate"
        COMPANY = "company", "Company"
        ORGANIZATION = "organization", "Organization"
        ADMIN = "admin", "Admin"

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.GRADUATE)

    REQUIRED_FIELDS = ["email"]  # keep username for simplicity
