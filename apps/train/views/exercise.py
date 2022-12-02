from rest_framework.viewsets import ModelViewSet

from apps.train.models import (
    Exercise,
    ExerciseCategory,
    ExerciseGroup,
    ExerciseItem,
    ExerciseSet,
)
from apps.train.serializers import (
    ExerciseCategorySerializer,
    ExerciseGroupSerializer,
    ExerciseItemSerializer,
    ExerciseSerializer,
    ExerciseSetSerializer,
)


class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.all().order_by("id")
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        exercise_group = self.request.data.get("exercise_group")

        query = Exercise.objects.filter(exercise_group=exercise_group)

        return query


class ExerciseGroupViewSet(ModelViewSet):
    queryset = ExerciseGroup.objects.all().order_by("id")
    serializer_class = ExerciseGroupSerializer

    def get_queryset(self):
        workout_plan = self.request.data.get("workout_plan")

        query = ExerciseGroup.objects.filter(workout_plan=workout_plan)

        return query


class ExerciseSetViewSet(ModelViewSet):
    queryset = ExerciseSet.objects.all().order_by("id")
    serializer_class = ExerciseSetSerializer

    def get_queryset(self):
        exercise = self.request.data.get("exercise")

        query = ExerciseSet.objects.filter(exercise=exercise)

        return query


class ExerciseCategoryViewSet(ModelViewSet):
    queryset = ExerciseCategory.objects.all().order_by("id")
    serializer_class = ExerciseCategorySerializer


class ExerciseItemViewSet(ModelViewSet):
    queryset = ExerciseItem.objects.all().order_by("label")
    serializer_class = ExerciseItemSerializer
