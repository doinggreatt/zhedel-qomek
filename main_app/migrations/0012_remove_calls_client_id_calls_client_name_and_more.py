# Generated by Django 5.0.1 on 2024-02-06 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_calls_category_alter_calls_time_accepted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calls',
            name='client_id',
        ),
        migrations.AddField(
            model_name='calls',
            name='client_name',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AlterField(
            model_name='calls',
            name='client_phone',
            field=models.CharField(max_length=11),
        ),
    ]
