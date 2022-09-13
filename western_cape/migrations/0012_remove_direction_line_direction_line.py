# Generated by Django 4.0.5 on 2022-09-13 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('western_cape', '0011_remove_line_direction_direction_line_direction_stops_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direction',
            name='line',
        ),
        migrations.AddField(
            model_name='direction',
            name='line',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='western_cape.line'),
        ),
    ]
