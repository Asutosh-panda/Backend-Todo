from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from .serializer import Todoserializer,Userserializer,UserSerializerWithToken
from .models import TodoList

from django.contrib.auth.forms import UserCreationForm
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.views import APIView

@api_view(['GET'])
def current_user(request):
    return Response(request.user.id)


class UserList(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def index(request):
    print(request.user)
    todolist= TodoList.objects.filter(user=request.user)
    serializer = Todoserializer(todolist,many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def registerpage(request):
         serializer = Userserializer(data=request.data)
         if serializer.is_valid():
                form = UserCreationForm(serializer.data)
                if form.is_valid():
                    form.save()
                else:
                    return Response(serializer.errors)
         return Response(serializer.errors)

    
@api_view(['GET'])
def getuser(request):
    return Response(request.user.id)

@api_view(['POST'])
def indexpost(request):
    serializer= Todoserializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)



@api_view(['PATCH'])
def indexput(request,pk):
    todo= TodoList.objects.get(id=pk)
    serializer=Todoserializer(instance=todo,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['DELETE'])
def indexdelete(request,pk):
    try:
        todo= TodoList.objects.get(id=pk)
        todo.delete()
        return Response("deleted")
    except:
        return Response("value not present")
