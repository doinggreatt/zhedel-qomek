# Generated by Django 5.0.1 on 2024-02-05 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_carsposition_is_free'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsposition',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main_app.cars', unique=True, verbose_name='id машины'),
        ),
    ]
