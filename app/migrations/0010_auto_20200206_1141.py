# Generated by Django 2.2.6 on 2020-02-06 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200206_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dtr',
            name='hours',
        ),
        migrations.RemoveField(
            model_name='dtr',
            name='minutes',
        ),
        migrations.AddField(
            model_name='dtr',
            name='diff',
            field=models.DurationField(null=True),
        ),
    ]
