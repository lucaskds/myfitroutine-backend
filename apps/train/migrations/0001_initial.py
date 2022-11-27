# Generated by Django 4.0.7 on 2022-11-26 21:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Exercise",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=256)),
                ("position", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="WorkoutPlan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(default="WorkoutPlan", max_length=256)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-label"],
            },
        ),
        migrations.CreateModel(
            name="ExerciseSet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("weight", models.IntegerField()),
                ("reps", models.IntegerField()),
                ("rest", models.IntegerField()),
                ("comment", models.TextField(blank=True, max_length=500)),
                (
                    "exercise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="train.exercise"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ExerciseGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.IntegerField()),
                (
                    "workout_plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="train.workoutplan",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="exercise",
            name="exercise_group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="train.exercisegroup"
            ),
        ),
    ]
