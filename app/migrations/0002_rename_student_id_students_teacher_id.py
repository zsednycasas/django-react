# Generated by Django 5.0 on 2024-01-05 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='student_id',
            new_name='teacher_id',
        ),
    ]
