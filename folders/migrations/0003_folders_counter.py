# Generated by Django 3.2.4 on 2022-06-24 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folders', '0002_auto_20220624_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='folders',
            name='counter',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество загрузок'),
        ),
    ]
