# Generated by Django 3.2.8 on 2021-10-29 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistics_counter', '0008_statictics_data_test_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statictics_data',
            name='test_field',
        ),
    ]