from rest_framework import serializers

from apps.train.models import WorkoutPlan


class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = ["id", "user", "label"]
