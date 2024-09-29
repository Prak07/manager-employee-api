import uuid
from django.db import models


class Manager(models.Model):
    id = models.AutoField(primary_key=True,editable=False, unique=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email = models.EmailField(unique=True)
    date_joined = models.DateField()
    createdat=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updatedat=models.DateTimeField(auto_now=True,null=True,blank=True)
    department = models.CharField(max_length=100)

class Employee(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email = models.EmailField(unique=True)
    date_joined = models.DateField()
    createdat=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updatedat=models.DateTimeField(auto_now=True,null=True,blank=True)
    designation = models.CharField(max_length=100)
    manager=models.ForeignKey(Manager,on_delete=models.SET_NULL,related_name='employees',null=True,blank=True)