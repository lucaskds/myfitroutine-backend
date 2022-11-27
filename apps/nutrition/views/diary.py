from rest_framework.viewsets import ModelViewSet

from apps.nutrition.models import NutritionDiary
from apps.nutrition.serializers import NutritionDiarySerializer


class NutritionDiaryViewSet(ModelViewSet):
    queryset = NutritionDiary.objects.all()
    serializer_class = NutritionDiarySerializer
