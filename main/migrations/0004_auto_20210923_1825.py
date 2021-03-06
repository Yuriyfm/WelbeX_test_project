# Generated by Django 3.2.5 on 2021-09-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210923_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='distance',
            field=models.IntegerField(db_index=True, verbose_name='Расстояние'),
        ),
        migrations.AlterField(
            model_name='table',
            name='quantity',
            field=models.IntegerField(db_index=True, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='table',
            name='title',
            field=models.CharField(db_index=True, max_length=40, verbose_name='Название'),
        ),
    ]
