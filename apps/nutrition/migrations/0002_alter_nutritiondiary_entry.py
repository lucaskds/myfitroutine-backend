# Generated by Django 4.0.7 on 2022-11-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutritiondiary',
            name='entry',
            field=models.JSONField(default=list),
        ),
    ]
