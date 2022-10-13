# Generated by Django 4.1.1 on 2022-10-13 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('country', models.CharField(max_length=50)),
                ('is_active', models.BooleanField()),
            ],
        ),
    ]