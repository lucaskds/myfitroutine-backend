from rest_framework import routers

from apps.nutrition.views import (
    FoodCategoryViewSet,
    FoodItemViewSet,
    NutritionDiaryViewSet,
)

app_name = "nutrition"

router = routers.SimpleRouter()

router.register("food/item", FoodItemViewSet, basename="nutrition")
router.register("food/category", FoodCategoryViewSet, basename="nutrition")
router.register("diary", NutritionDiaryViewSet, basename="nutrition")

urlpatterns = [] + router.urls
