from rest_framework.viewsets import ModelViewSet

from apps.train.models import WorkoutDiary
from apps.train.serializers import WorkoutDiarySerializer


class WorkoutDiaryViewSet(ModelViewSet):
    queryset = WorkoutDiary.objects.all().order_by_date()
    serializer_class = WorkoutDiarySerializer

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)

        return queryset

    def create(self, request, *args, **kwargs):
        kwargs["user"] = request.user
        return super().create(request, *args, **kwargs)
