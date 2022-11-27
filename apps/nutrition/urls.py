from rest_framework import routers

from apps.nutrition.views import (
    FoodCategoryViewSet,
    FoodItemViewSet,
    NutritionDiaryViewSet,
)

app_name = "nutrition"

router = routers.SimpleRouter()

router.register("food/item", FoodItemViewSet)
router.register("food/category", FoodCategoryViewSet)
router.register("diary", NutritionDiaryViewSet)

urlpatterns = [] + router.urls
