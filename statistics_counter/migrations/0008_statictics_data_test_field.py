# Generated by Django 3.2.8 on 2021-10-29 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics_counter', '0007_auto_20211027_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='statictics_data',
            name='test_field',
            field=models.CharField(default='No', max_length=255, verbose_name='test'),
        ),
    ]
