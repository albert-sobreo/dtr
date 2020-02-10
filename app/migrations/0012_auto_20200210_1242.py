# Generated by Django 2.2.6 on 2020-02-10 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='dtr',
        ),
        migrations.AddField(
            model_name='account',
            name='dtr',
            field=models.ManyToManyField(blank=True, to='app.DTR'),
        ),
    ]
