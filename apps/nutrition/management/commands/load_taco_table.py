import csv
import os
from django.conf import settings
from django.core.management.base import BaseCommand

from apps.nutrition.models import FoodCategory, FoodItem


class Command(BaseCommand):
    help = "Load TACO info to DB."

    def handle(self, *args, **options):
        file = open(os.path.join(settings.BASE_DIR, "base_data/TACO.csv"))
        read_file = csv.reader(file)

        for record in read_file:
            category, _ = FoodCategory.objects.get_or_create(label=record[0])
            FoodItem.objects.get_or_create(
                category=category,
                label=record[1],
                kcal=record[2] or None,
                protein=record[3] or None,
                fat=record[4] or None,
                carbs=record[5] or None,
                fibers=record[6] or None,
            )
