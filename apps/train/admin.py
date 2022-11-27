from django.contrib import admin

from apps.train.models import Exercise, ExerciseGroup, ExerciseSet, WorkoutPlan

admin.site.register(Exercise)
admin.site.register(ExerciseGroup)
admin.site.register(ExerciseSet)
admin.site.register(WorkoutPlan)
