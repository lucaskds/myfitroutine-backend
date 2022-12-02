from django.contrib import admin

from apps.nutrition.models import FoodCategory, FoodItem, NutritionDiary

admin.site.register(FoodCategory)
admin.site.register(NutritionDiary)
import csv
import os

from django.conf import settings


@admin.action(description="Update food item table")
def update_list(modeladmin, request, queryset):
    file = open(os.path.join(settings.BASE_DIR, "base_data/TACO.csv"))
    read_file = csv.reader(file)

    for record in read_file:
        category, _ = FoodCategory.objects.get_or_create(label=record[0])
        FoodItem.objects.get_or_create(
            category=category,
            label=record[1],
            kcal=record[2] or None,
            protein=record[3] or None,
            fat=record[4] or None,
            carbs=record[5] or None,
            fibers=record[6] or None,
        )


class FoodItemAdmin(admin.ModelAdmin):
    list_display = ["category", "label"]
    ordering = ["label"]
    actions = [update_list]


admin.site.register(FoodItem, FoodItemAdmin)
