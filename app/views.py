from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentsSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, logout
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=request.data['username'])
        token = Token.objects.get(user=user)

        serializer = UserSerializer(user)

        data = {
            "user": serializer.data,
            "token": token.key
        }

        return Response(data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "sign up page"})

@api_view(['POST'])
def login(request):

    data = request.data
    authenticate_user = authenticate(username=data['username'], password=data['password'])

    if authenticate_user is not None:
        user = User.objects.get(username=data['username'])
        serializer = UserSerializer(user)

        response_data = {
            'user': serializer.data,

        }

        token, created_token = Token.objects.get_or_create(user=user)

        if token:
            response_data['token'] = token.key
        elif created_token: 
            response_data['token'] = created_token.key
        
        return Response(response_data)

    return Response({"detail": "not found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def TestView(request):

    return Response({"message": "Test view page"})

@api_view(['POST'])
def logout(request):

    return Response({"message": "Logout page"})




#CREATE
#Create Students
@api_view(['POST'])
def CreateStudent(request):
    if request.method == 'POST':
        username = request.data.get('username', None)

        # Check if the username already exists
        if Students.objects.filter(username=username).exists():
            return Response({
                'message': 'Username already exists. Please choose a different username.'
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Student added successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            'message': 'Error adding student',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
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
