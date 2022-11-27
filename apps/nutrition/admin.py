from django.contrib import admin
from apps.nutrition.models import FoodCategory, FoodItem, NutritionDiary

admin.site.register(FoodCategory)
admin.site.register(FoodItem)
admin.site.register(NutritionDiary)
