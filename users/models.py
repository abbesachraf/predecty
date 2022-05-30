from pickle import TRUE
from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=20, default='', null=False)
    last = models.CharField(max_length=20, default='', null=False)
    email = models.EmailField(max_length = 150)
    message = models.CharField(max_length=20, default='', null=False)
    def __str__(self):
        return self.name



class Result1 (models.Model):
    n1=models.CharField(max_length=20,default='',null=False)
    username=models.CharField(max_length=20,default='',null=False)
    email=models.CharField(max_length=25,default='',null=False)
    def __str__(self):
        return self.n1
    
