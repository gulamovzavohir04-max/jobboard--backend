from django.conf import settings
from django.db import models

class Job(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="jobs"
    )
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
