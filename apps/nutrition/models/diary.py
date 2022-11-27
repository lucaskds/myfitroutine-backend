from django.conf import settings
from django.db import models


class NutritionDiary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    entry = models.JSONField()
