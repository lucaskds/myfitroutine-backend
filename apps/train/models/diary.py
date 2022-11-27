from django.conf import settings
from django.db import models


class WorkoutDiary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    entry = models.JSONField(default=list)
    duration = models.PositiveIntegerField(default=0)
    comments = models.TextField(max_length=500, blank=True)
