# Generated by Django 5.0.1 on 2024-02-05 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_cars_is_working'),
    ]

    operations = [
        migrations.AddField(
            model_name='carsposition',
            name='is_free',
            field=models.BooleanField(default=True),
        ),
    ]
