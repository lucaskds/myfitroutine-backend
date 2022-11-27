from rest_framework import serializers

from apps.nutrition.models import NutritionDiary


class NutritionDiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionDiary
        fields = ["user", "date", "entry"]
