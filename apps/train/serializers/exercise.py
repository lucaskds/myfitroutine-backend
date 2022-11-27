from rest_framework import serializers

from apps.train.models import Exercise, ExerciseGroup, ExerciseSet


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["exercise_group", "label", "position"]


class ExerciseGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseGroup
        fields = ["workout_plan", "position"]


class ExerciseSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseSet
        fields = ["exercise", "weight", "reps", "rest", "comment"]
