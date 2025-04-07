from django.db import models

# Create your models here.

class admissionDb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    course=models.CharField(max_length=100,null=True,blank=True)
    number=models.IntegerField(null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    message=models.CharField(max_length=500,null=True,blank=True)

class contactDb(models.Model):
    Cname=models.CharField(max_length=100,null=True,blank=True)

    Cnumber=models.IntegerField(null=True,blank=True)
    Cemail=models.EmailField(max_length=100,null=True,blank=True)
    Cmessage=models.CharField(max_length=500,null=True,blank=True)
