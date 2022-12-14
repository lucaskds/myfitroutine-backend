# Generated by Django 3.2.16 on 2022-12-02 00:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("train", "0004_workoutdiary_comments_workoutdiary_duration"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExerciseCategory",
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
            ],
        ),
        migrations.CreateModel(
            name="ExerciseItem",
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
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="train.exercisecategory",
                    ),
                ),
            ],
        ),
    ]
