from django.db import models

# Create your models here.

#Students Model
class Students(models.Model):
    student_id = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=200, default='default_password_here')

    def __str__(self):
        return self.student_id

#Teacher Model
class Teacher(models.Model):
    teacher_id = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)

    def __str__(self):
        return self.teacher_id