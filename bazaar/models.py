from datetime import date
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    englishname=models.CharField(max_length=300)
    hindiname=models.CharField(max_length=300)
    photo= models.ImageField(upload_to='images/categories/',null=True,blank=True)
    def __str__(self):
        return self.englishname


class Product(models.Model):
    englishname=models.CharField(max_length=300)
    hindiname=models.CharField(max_length=300)
    photo= models.ImageField(upload_to='images/products/',null=True,blank=True)
    categoryid=models.PositiveIntegerField(null=True)
    categoryname=models.CharField(max_length=200,null=True)
    price=models.PositiveIntegerField(null=True)
    quantity=models.CharField(max_length=100)
    def __str__(self):
        return self.englishname

class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    category=models.ForeignKey( Category,on_delete=models.CASCADE,null=True)
    price=models.PositiveIntegerField(null=True)
    customername=models.CharField(max_length=200,null=True)
    mobile=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=500,null=True)
    date=models.DateField(auto_now=True)