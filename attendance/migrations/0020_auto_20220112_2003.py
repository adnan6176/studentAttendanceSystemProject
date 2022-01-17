# Generated by Django 3.2.11 on 2022-01-12 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0019_remove_attendance_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='teacher',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date_present',
            field=models.DateField(blank=True),
        ),
    ]