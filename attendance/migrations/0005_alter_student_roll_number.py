# Generated by Django 3.2.11 on 2022-01-12 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_alter_student_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.IntegerField(blank=True, max_length=10),
        ),
    ]
