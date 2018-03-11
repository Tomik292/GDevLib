from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=50)
    recipient = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    sedingTime = models.DateTimeField()


    
    
