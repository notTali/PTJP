# Generated by Django 4.0.5 on 2022-09-13 03:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('western_cape', '0002_remove_direction_line_remove_direction_trains_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='direction',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='western_cape.direction'),
        ),
    ]
