# Generated by Django 4.1.3 on 2022-12-22 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_alter_volunteer_hour_volunteer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer_hour',
            name='end',
            field=models.TimeField(default=None, null=True),
        ),
    ]