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
    queryset = Exercise.objects.order_by("id")
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        exercise_group = self.request.GET.get("exercise_group")

        if not exercise_group:
            return self.queryset

        query = self.queryset.filter(exercise_group=exercise_group)

        return query


class ExerciseGroupViewSet(ModelViewSet):
    queryset = ExerciseGroup.objects.order_by("id")
    serializer_class = ExerciseGroupSerializer

    def get_queryset(self):
        workout_plan = self.request.GET.get("workout_plan")

        if not workout_plan:
            return self.queryset

        query = self.queryset.filter(workout_plan=workout_plan)

        return query


class ExerciseSetViewSet(ModelViewSet):
    queryset = ExerciseSet.objects.order_by("id")
    serializer_class = ExerciseSetSerializer

    def get_queryset(self):
        exercise = self.request.GET.get("exercise")

        if not exercise:
            return self.queryset

        query = self.queryset.filter(exercise=exercise)

        return query


class ExerciseCategoryViewSet(ModelViewSet):
    queryset = ExerciseCategory.objects.all().order_by("id")
    serializer_class = ExerciseCategorySerializer


class ExerciseItemViewSet(ModelViewSet):
    queryset = ExerciseItem.objects.all().order_by("label")
    serializer_class = ExerciseItemSerializer
