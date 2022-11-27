from rest_framework.viewsets import ModelViewSet

from apps.train.models import WorkoutDiary
from apps.train.serializers import WorkoutDiarySerializer


class WorkoutDiaryViewSet(ModelViewSet):
    queryset = WorkoutDiary.objects.all().order_by("date")
    serializer_class = WorkoutDiarySerializer
