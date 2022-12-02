import csv
import os
from django.conf import settings
from django.core.management.base import BaseCommand

from apps.train.models import ExerciseItem, ExerciseCategory


class Command(BaseCommand):
    help = "Load exercises list to DB."

    def handle(self, *args, **options):
        file = open(os.path.join(settings.BASE_DIR, "base_data/exercises.csv"))
        read_file = csv.reader(file)

        for record in read_file:
            category, _ = ExerciseCategory.objects.get_or_create(label=record[0])
            ExerciseItem.objects.get_or_create(
                category=category,
                label=record[1],
            )
