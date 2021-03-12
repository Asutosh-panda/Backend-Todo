from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import Todoserializer
from .models import TodoList
# Create your views here.

@api_view(['GET'])
def index(request):
    todolist= TodoList.objects.all()
    serializer = Todoserializer(todolist,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def indexpost(request):
    serializer= Todoserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response("error")


@api_view(['PUT'])
def indexput(request,pk):
    todo= TodoList.objects.get(id=pk)
    serializer=Todoserializer(instance=todo,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response("error")

@api_view(['DELETE'])
def indexdelete(request,pk):
    try:
        todo= TodoList.objects.get(id=pk)
        todo.delete()
        return Response("deleted")
    except:
        return Response("value not present")

#instance=TodoList,