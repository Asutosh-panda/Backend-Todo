from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class TodoList(models.Model):

    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, null=True)
    title=models.CharField(max_length=122)
    status=models.BooleanField()
    date=models.DateField()

    def __str__(self):
        return self.title

class UserList(models.Model):
    username= models.CharField(max_length=122)
    password1= models.CharField(max_length=122)
    password2= models.CharField(max_length=122)
    