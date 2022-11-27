from django.db import models
from django.conf import settings


class NutritionDiary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    entry = models.JSONField()
