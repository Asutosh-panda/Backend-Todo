from django.db import models

# Create your models here.

class TodoList(models.Model):
    title=models.CharField(max_length=122)
    status=models.BooleanField()
    date=models.DateField()

    def __str__(self):
        return self.title