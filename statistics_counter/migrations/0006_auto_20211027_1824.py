# Generated by Django 3.2.8 on 2021-10-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics_counter', '0005_auto_20211024_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statictics_data',
            name='cpc',
            field=models.FloatField(verbose_name='Cредняя стоимость клика'),
        ),
        migrations.AlterField(
            model_name='statictics_data',
            name='cpm',
            field=models.FloatField(verbose_name='Cредняя стоимость 1000 показов'),
        ),
    ]
