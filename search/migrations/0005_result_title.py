# Generated by Django 4.0.5 on 2022-09-26 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_alter_result_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
