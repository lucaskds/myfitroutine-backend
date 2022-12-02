from django.db import models


class Exercise(models.Model):
    exercise_group = models.ForeignKey("ExerciseGroup", on_delete=models.CASCADE)
    label = models.CharField(max_length=256)
    position = models.IntegerField()


class ExerciseGroup(models.Model):
    workout_plan = models.ForeignKey("WorkoutPlan", on_delete=models.CASCADE)
    position = models.IntegerField()


class ExerciseSet(models.Model):
    exercise = models.ForeignKey("Exercise", on_delete=models.CASCADE)
    weight = models.IntegerField()
    reps = models.IntegerField()
    rest = models.IntegerField()
    comment = models.TextField(max_length=500, blank=True)


class ExerciseCategory(models.Model):
    label = models.CharField(max_length=256)


class ExerciseItem(models.Model):
    category = models.ForeignKey("ExerciseCategory", on_delete=models.CASCADE)
    label = models.CharField(max_length=256)
