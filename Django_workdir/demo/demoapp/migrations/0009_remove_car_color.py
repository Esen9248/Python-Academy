# Generated by Django 2.0.2 on 2018-03-12 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0008_remove_car_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='color',
        ),
    ]
