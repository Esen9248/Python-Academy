# Generated by Django 2.0.2 on 2018-03-14 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0010_car_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='brand',
        ),
    ]