# Generated by Django 2.0.2 on 2018-03-09 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0005_auto_20180307_1543'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Colors',
            new_name='Brand',
        ),
        migrations.RenameModel(
            old_name='Brands',
            new_name='Color',
        ),
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
    ]
