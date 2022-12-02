from django.contrib import admin

from apps.train.models import (
    Exercise,
    ExerciseCategory,
    ExerciseGroup,
    ExerciseItem,
    ExerciseSet,
    WorkoutDiary,
    WorkoutPlan,
)

admin.site.register(Exercise)
admin.site.register(ExerciseGroup)
admin.site.register(ExerciseSet)
admin.site.register(ExerciseCategory)
admin.site.register(WorkoutPlan)
admin.site.register(WorkoutDiary)

import csv
import os

from django.conf import settings

from apps.train.models import ExerciseCategory, ExerciseItem


@admin.action(description="Update exercises table")
def update_list(modeladmin, request, queryset):
    file = open(os.path.join(settings.BASE_DIR, "base_data/exercises.csv"))
    read_file = csv.reader(file)

    for record in read_file:
        category, _ = ExerciseCategory.objects.get_or_create(label=record[0])
        ExerciseItem.objects.get_or_create(
            category=category,
            label=record[1],
        )


class ExerciseItemAdmin(admin.ModelAdmin):
    list_display = ["category", "label"]
    ordering = ["label"]
    actions = [update_list]


admin.site.register(ExerciseItem, ExerciseItemAdmin)
