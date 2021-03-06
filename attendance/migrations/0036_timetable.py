# Generated by Django 3.2.11 on 2022-01-23 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0035_auto_20220122_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednessday', 'Wednessday'), ('Thrusday', 'Thrusday'), ('Friday', 'Friday')], max_length=20, null=True)),
                ('period', models.CharField(blank=True, choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], max_length=20, null=True)),
                ('class_name', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='attendance.classid')),
                ('teacher', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
