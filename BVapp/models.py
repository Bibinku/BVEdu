from django.db import models

# Create your models here

class courseDB(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    time = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    description2 = models.CharField(max_length=500, null=True, blank=True)
    price =models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to="images", null=True, blank=True)
