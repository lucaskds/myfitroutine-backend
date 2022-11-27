from rest_framework.viewsets import ModelViewSet

from apps.train.models import WorkoutPlan
from apps.train.serializers import WorkoutPlanSerializer


class WorkoutViewSet(ModelViewSet):
    queryset = WorkoutPlan.objects.all().order_by("label")
    serializer_class = WorkoutPlanSerializer

    def get_queryset(self):
        query_param = self.request.query_params.get("workout")

        if query_param:
            return self.queryset.filter(label__istartswith=query_param)[:5]

        return self.queryset
