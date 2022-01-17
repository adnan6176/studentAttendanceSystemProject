# Generated by Django 3.2.11 on 2022-01-12 11:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0010_attendance_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='date_present',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
