from rest_framework import routers

from apps.train.views import (
    ExerciseViewSet,
    ExerciseGroupViewSet,
    ExerciseSetViewSet,
    WorkoutViewSet,
)

app_name = "training"

router = routers.SimpleRouter()

router.register(r"exercises/group", ExerciseGroupViewSet, basename="exercise")
router.register(r"exercises/exercise", ExerciseViewSet)
router.register(r"exercises/set", ExerciseSetViewSet)
router.register(r"workouts", WorkoutViewSet, basename="workout")

urlpatterns = [] + router.urls
