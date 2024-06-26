from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
'''
class Profile(models.Model):
    user=models.OneToOneField(User , on_delete=models.CASCADE)
    email_token=models.CharField(max_length=200)
    is_verified=models.BooleanField(default=False)
    def __str__(self):
        return self.user'''


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=20, default='', null=False)
    mobileC = models.CharField(max_length=20, default='', null=False)
    email = models.EmailField(max_length = 150)
    message = models.CharField(max_length=20, default='', null=False)
    #id = models.AutoField(primary_key=True,unique=False,auto_created=True, null=False)
    def __str__(self):
        return self.email



class Result1 (models.Model):
    rzlt=models.CharField(max_length=20,default='',null=False)
    username=models.CharField(max_length=20,default='',null=False)
    email=models.CharField(max_length=25,default='',null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.rzlt
    
