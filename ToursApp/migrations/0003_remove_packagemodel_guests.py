# Generated by Django 4.1.4 on 2023-01-05 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToursApp', '0002_packagemodel_place_info_alter_packagemodel_tour_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packagemodel',
            name='guests',
        ),
    ]
