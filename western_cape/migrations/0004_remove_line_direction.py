# Generated by Django 4.0.5 on 2022-09-13 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('western_cape', '0003_alter_line_direction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='line',
            name='direction',
        ),
    ]
