# Generated by Django 3.2.11 on 2022-01-12 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0016_alter_attendance_teacher_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='student_id',
        ),
    ]