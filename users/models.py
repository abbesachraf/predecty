from pickle import TRUE
from django.db import models


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
    
class Order(models.Model):
    product_category = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)
    shipping_cost = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
