# Generated by Django 5.0.1 on 2024-02-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_delete_clients_carsposition_call_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calls',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]