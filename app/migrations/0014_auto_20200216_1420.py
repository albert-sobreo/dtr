# Generated by Django 2.2.6 on 2020-02-16 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20200210_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='fuck',
            field=models.ManyToManyField(blank=True, related_name='fuck', to='app.DTR'),
        ),
        migrations.AlterField(
            model_name='account',
            name='dtr',
            field=models.ManyToManyField(blank=True, related_name='dtr', to='app.DTR'),
        ),
    ]