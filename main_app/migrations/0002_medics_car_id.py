# Generated by Django 5.0.1 on 2024-02-03 04:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medics',
            name='car_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='main_app.cars'),
        ),
    ]
