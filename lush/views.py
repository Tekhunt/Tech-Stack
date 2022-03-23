from django.shortcuts import render
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task


# Create your views here.
@api_view(['GET'])
def home(request):
    return Response({'routes':{
        '/': 'home',
        '/create': "create user",
        '/get': 'get all users',
        '/details': 'get a single user details',
        '/update': 'update a user record',
        '/delete': 'delete a user record'
    }})
    
@api_view(['POST'])
def createTask(request):
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def getTask(request):
    task  = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def details(request, pk):
    task  = Task.objects.get(pk=pk)
    serializer = TaskSerializer(instance=task, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateTask(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Task.objects.get(pk=pk).delete()
    return Response('Task successfullt deleted')

