# Generated by Django 4.1.4 on 2023-01-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToursApp', '0006_myprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('contact', models.IntegerField()),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='MyProfile',
        ),
    ]
