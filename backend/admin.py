from django.contrib import admin
from backend.models import TodoList,UserList
# Register your models here.
admin.site.register(TodoList)
admin.site.register(UserList)