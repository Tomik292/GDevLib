from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.PROTECT)
    recipient = models.CharField(max_length=50)
    subject = models.CharField(max_length=50, default = "Subject")
    text = models.TextField(max_length=500)
    sedingTime = models.DateTimeField()

    def __str__(self):
        return "From:" + str(self.sender) + " To:"+(self.recipient) + " at:" + str(self.sedingTime)


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    engine = models.CharField(max_length=50)

    def __str__(self):
        return self.engine + " " + self.name;

class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField()
    bio = models.TextField(max_length=500)
    favorite_categories = models.ManyToManyField(Category)
    location = models.CharField(max_length=50)

    @receiver(post_save, sender=User)
    def create_user_extension(sender, instance, created, **kwargs):
       if created:
           UserExtension.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userextension.save()

    def __str__(self):
        return str(self.user) + "'s extension"


    
