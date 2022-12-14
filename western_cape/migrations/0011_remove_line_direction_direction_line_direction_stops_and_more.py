# Generated by Django 4.0.5 on 2022-09-13 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('western_cape', '0010_remove_direction_line_line_direction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='line',
            name='direction',
        ),
        migrations.AddField(
            model_name='direction',
            name='line',
            field=models.ManyToManyField(to='western_cape.line'),
        ),
        migrations.AddField(
            model_name='direction',
            name='stops',
            field=models.ManyToManyField(to='western_cape.stop'),
        ),
        migrations.AddField(
            model_name='line',
            name='train_stop_time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='western_cape.arrival'),
        ),
    ]
