# Generated by Django 4.0.7 on 2022-11-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0002_workoutdiary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutdiary',
            name='entry',
            field=models.JSONField(default=list),
        ),
    ]