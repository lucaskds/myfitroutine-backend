from rest_framework.viewsets import ModelViewSet

from apps.nutrition.models import FoodCategory, FoodItem, NutritionDiary
from apps.nutrition.serializers import (
    FoodCategorySerializer,
    FoodItemSerializer,
    NutritionDiarySerializer,
)


class FoodCategoryViewSet(ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer


class FoodItemViewSet(ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer


class NutritionDiaryViewSet(ModelViewSet):
    queryset = NutritionDiary.objects.all()
    serializer_class = NutritionDiarySerializer
