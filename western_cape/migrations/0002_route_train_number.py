# Generated by Django 4.0.5 on 2022-09-13 01:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('western_cape', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='train_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
