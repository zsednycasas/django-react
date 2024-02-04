# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Students, Teacher

#User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email','password']

# Students Serializer
class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['student_id', 'first_name', 'middle_name', 'last_name', 'address', 'contact', 'username', 'password']


#Teachers Serializer
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['teacher_id', 'first_name', 'middle_name','last_name','address','contact']
        
