# models are simply  how we create database tables

from django.db import models  
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description= models.TextField(max_length=500)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['complete']

class userInfo(models.Model):
    Username = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    Confirm = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.username
    

        