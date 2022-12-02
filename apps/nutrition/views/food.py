from rest_framework.viewsets import ModelViewSet

from apps.nutrition.models import FoodCategory, FoodItem
from apps.nutrition.serializers import FoodCategorySerializer, FoodItemSerializer


class FoodCategoryViewSet(ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer


class FoodItemViewSet(ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
