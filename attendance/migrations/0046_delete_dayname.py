# Generated by Django 3.2.11 on 2022-01-23 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0045_alter_timetable_day'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DayName',
        ),
    ]
