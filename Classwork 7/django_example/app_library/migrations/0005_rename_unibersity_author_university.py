# Generated by Django 4.1.1 on 2022-10-13 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_library', '0004_author_birth_date_author_city_author_country_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='unibersity',
            new_name='university',
        ),
    ]
