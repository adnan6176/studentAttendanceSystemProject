# Generated by Django 3.2.11 on 2022-01-12 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_alter_student_roll_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.IntegerField(blank=True),
        ),
    ]
