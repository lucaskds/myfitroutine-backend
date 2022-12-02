from rest_framework import routers
from django.urls import path
from apps.train.views import (
    ExerciseGroupViewSet,
    ExerciseSetViewSet,
    ExerciseViewSet,
    ExerciseCategoryViewSet,
    ExerciseItemViewSet,
    WorkoutViewSet,
    WorkoutDiaryViewSet,
)

app_name = "training"

router = routers.SimpleRouter()

router.register("exercises/group", ExerciseGroupViewSet, basename="exercise")
router.register("exercises/exercise", ExerciseViewSet)
router.register("exercises/set", ExerciseSetViewSet)
router.register("workouts", WorkoutViewSet, basename="workout")
router.register("diary", WorkoutDiaryViewSet)

urlpatterns = [] + router.urls

urlpatterns += [
    path(
        "exercises/item",
        ExerciseItemViewSet.as_view(
            {
                "get": "list",
            },
        ),
        name="exercise-items",
    ),
    path(
        "exercises/category",
        ExerciseCategoryViewSet.as_view(
            {
                "get": "list",
            },
        ),
        name="exercise-categories",
    ),
]
