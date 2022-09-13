# Generated by Django 4.0.5 on 2022-09-13 12:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('western_cape', '0006_arrival_platform_number_alter_arrival_arrival_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direction',
            name='stops',
        ),
        migrations.AddField(
            model_name='stop',
            name='direction',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='western_cape.direction'),
        ),
    ]
