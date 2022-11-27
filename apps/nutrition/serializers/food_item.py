from rest_framework import serializers

from apps.nutrition.models import FoodItem, FoodCategory


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = ["label"]


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ["category", "label", "kcal", "protein", "fat", "carbs", "fibers"]
