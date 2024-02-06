# backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from .models import Students

class StudentBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            student = Students.objects.get(username=username)
        except Students.DoesNotExist:
            return None

        if check_password(password, student.password):
            return student
