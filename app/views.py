from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentsSerializer

#CREATE
#Create Student
@api_view(['POST'])
def CreateStudent(request):
    if request.method == 'POST':
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#READ
#Get All Students
@api_view(['GET'])
def GetAllStudents(request):
    get_posts = Students.objects.all()
    serializer = StudentsSerializer(get_posts, many=True)
    
    return Response(serializer.data)

#UPDATE
#Edit for the student
@api_view(['GET', 'PUT'])
def EditStudent(request, pk):
    student = get_object_or_404(Students, pk=pk)

    if request.method == 'GET':
        serializer = StudentsSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentsSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#DELETE
#Delete for the student   
@api_view(['DELETE'])
def DeleteStudent(request, pk):
    student = get_object_or_404(Students, pk=pk)
    
    student.delete()
    
    return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
