from rest_framework.viewsets import ModelViewSet

from apps.nutrition.models import NutritionDiary
from apps.nutrition.serializers import NutritionDiarySerializer


class NutritionDiaryViewSet(ModelViewSet):
    queryset = NutritionDiary.objects.all().order_by_date()
    serializer_class = NutritionDiarySerializer

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)

        return queryset

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        return super().create(request, *args, **kwargs)
