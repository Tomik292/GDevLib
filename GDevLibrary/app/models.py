from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.PROTECT)
    recipient = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    sedingTime = models.DateTimeField()

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    engine = models.CharField(max_length=50)

class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField()
    bio = models.TextField(max_length=500)
    favorite_categories = models.ManyToManyField(Category)
    location = models.CharField(max_length=50)



    
