# Generated by Django 4.1.1 on 2022-10-16 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name': 'вакансия', 'verbose_name_plural': 'вакансии'},
        ),
    ]