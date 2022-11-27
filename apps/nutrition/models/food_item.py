from django.db import models


class FoodCategory(models.Model):
    label = models.CharField(max_length=258)


class FoodItem(models.Model):
    category = models.ForeignKey("FoodCategory", on_delete=models.CASCADE)
    label = models.CharField(max_length=258)
    kcal = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()
    fibers = models.FloatField()
