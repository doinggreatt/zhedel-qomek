# Generated by Django 5.0.1 on 2024-02-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_carsposition_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='calls',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='calls',
            name='long',
            field=models.FloatField(default=0),
        ),
    ]
