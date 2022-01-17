# Generated by Django 3.2.11 on 2022-01-13 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0028_attendance_submit_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='classID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classCode', models.CharField(blank=True, max_length=2, null=True)),
                ('className', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='class_name',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='attendance.classid'),
        ),
    ]
