# Generated by Django 5.0.1 on 2024-02-05 16:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_calls_lat_calls_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calls',
            name='car_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main_app.cars', verbose_name='id кареты'),
        ),
    ]