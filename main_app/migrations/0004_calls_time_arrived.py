# Generated by Django 5.0.1 on 2024-02-03 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_calls_options_alter_cars_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='calls',
            name='time_arrived',
            field=models.DateTimeField(auto_now=True, verbose_name='Время прибытия на вызов'),
        ),
    ]
