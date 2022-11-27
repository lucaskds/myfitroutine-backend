from django.db import models


class FoodCategory(models.Model):
    label = models.CharField(max_length=258)


class FoodItem(models.Model):
    category = models.ForeignKey("FoodCategory", on_delete=models.CASCADE)
    label = models.CharField(max_length=258)
    kcal = models.FloatField(null=True)
    protein = models.FloatField(null=True)
    fat = models.FloatField(null=True)
    carbs = models.FloatField(null=True)
    fibers = models.FloatField(null=True)
