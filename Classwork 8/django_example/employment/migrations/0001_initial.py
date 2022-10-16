# Generated by Django 4.1.1 on 2022-10-16 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активность')),
                ('title', models.CharField(max_length=30, verbose_name='Заголовок')),
                ('description', models.TextField(default='', verbose_name='Описание')),
                ('publisher', models.CharField(max_length=30, verbose_name='Кто опубликовал')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('published_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
            ],
        ),
    ]