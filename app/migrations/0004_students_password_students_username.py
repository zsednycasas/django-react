# Generated by Django 5.0 on 2024-01-07 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_teacher_rename_teacher_id_students_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='password',
            field=models.CharField(default='default_password_here', max_length=200),
        ),
        migrations.AddField(
            model_name='students',
            name='username',
            field=models.CharField(default=12345, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
