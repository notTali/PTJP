# Generated by Django 4.0.5 on 2022-09-21 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('western_cape', '0026_remove_graphedge_interchange_stop_interchange'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphedge',
            name='lines',
            field=models.ManyToManyField(to='western_cape.line'),
        ),
    ]