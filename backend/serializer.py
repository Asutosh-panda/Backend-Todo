from rest_framework import serializers
from backend.models import TodoList

class Todoserializer(serializers.ModelSerializer):
    class Meta:
        model=TodoList
        fields="__all__"