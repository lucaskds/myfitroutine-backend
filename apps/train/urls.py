from rest_framework import routers

from apps.train.views import (
    ExerciseGroupViewSet,
    ExerciseSetViewSet,
    ExerciseViewSet,
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
