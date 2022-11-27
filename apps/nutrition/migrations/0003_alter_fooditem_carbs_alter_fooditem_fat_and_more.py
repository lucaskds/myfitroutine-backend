# Generated by Django 4.0.7 on 2022-11-27 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0002_alter_nutritiondiary_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='carbs',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='fat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='fibers',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='kcal',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='protein',
            field=models.FloatField(null=True),
        ),
    ]
