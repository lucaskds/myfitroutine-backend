from rest_framework import serializers

from apps.train.models import WorkoutDiary


class WorkoutDiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutDiary
        fields = ["user", "date", "entry"]
