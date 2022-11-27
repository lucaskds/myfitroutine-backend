from django.conf import settings
from django.db import models


class WorkoutPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    label = models.CharField(max_length=256, default="WorkoutPlan")

    class Meta:
        ordering = ["-label"]
