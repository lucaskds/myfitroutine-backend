from rest_framework import serializers

from apps.train.models import (
    Exercise,
    ExerciseGroup,
    ExerciseSet,
    ExerciseCategory,
    ExerciseItem,
)


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


class ExerciseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseCategory
        fields = ["label"]


class ExerciseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseItem
        fields = ["category", "label"]
