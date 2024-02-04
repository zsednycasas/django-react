# Generated by Django 5.0 on 2024-01-05 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_student_id_students_teacher_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='students',
            old_name='teacher_id',
            new_name='student_id',
        ),
    ]
