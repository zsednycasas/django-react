# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Students, Teacher
from rest_framework.authtoken.models import Token

#User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email','password']
    
    def save(self, **kwargs):
        new_user = User.objects.create_user(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            password=self.validated_data['password'],
        )
        new_user.save()

        new_token = Token.objects.create(user=new_user)

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
        
