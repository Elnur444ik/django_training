# Generated by Django 4.1.1 on 2022-10-06 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0004_advertisementstatus_alter_advertisement_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='status',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisements_app.advertisementstatus'),
        ),
    ]
