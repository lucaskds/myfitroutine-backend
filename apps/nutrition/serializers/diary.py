from rest_framework import serializers

from apps.nutrition.models import NutritionDiary


class NutritionDiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionDiary
        fields = ["user", "date", "entry"]

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        return super().create(request, *args, **kwargs)
