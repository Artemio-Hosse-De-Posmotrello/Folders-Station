# Generated by Django 3.2.4 on 2022-06-22 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5, verbose_name='Штамп Папки')),
                ('descrip', models.CharField(max_length=100, verbose_name='Краткое Описание')),
                ('datecomplited', models.DateField(blank=True, null=True, verbose_name='Дата Добавления Файла')),
                ('file', models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='Выберите Файл')),
            ],
        ),
    ]