from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchQuery
from cloudinary.models import CloudinaryField
from django import forms
from django.contrib import admin
#Create your models here.

def get_users_name(self):
    return self.first_name+" "+self.last_name

User.add_to_class("__str__", get_users_name)

 
class Category(models.Model):
    id_category = models.CharField(max_length=5)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class temple(models.Model): 
    id_temple = models.CharField(max_length=5)
    name = models.CharField(max_length=255) 
    Monk = models.CharField(max_length=255)
    Details = models.CharField(max_length=255)
    Detailsa = models.CharField(max_length=255)
    Detailsb = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    Longitude = models.CharField(max_length=255)
    image = CloudinaryField('image')
    Category = models.ManyToManyField(Category, blank=True)


    def __str__(self):
        return self.name

