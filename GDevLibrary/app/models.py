from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from .utils import ENGINE_CHOICES

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.PROTECT)
    recipient = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    sedingTime = models.DateTimeField()
    seen = models.BooleanField(default=False)

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

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length = 50)
    engine = models.CharField(choices=ENGINE_CHOICES, max_length = 10)
    text = models.TextField(max_length = 10000)
    tags = models.TextField(max_length = 200)
    picture = models.ImageField()
    verified = models.BooleanField()
    points = models.IntegerField(default = 0)

    def __str__(self):
       return "Article " + self.name + " by " + str(self.user) + " " + str(self.points) + " points"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField(max_length = 500)
    time = models.DateTimeField()
    points = models.IntegerField(default = 0)

    def __str__(self):
       return "Comment on article "+ str(self.article.name) + " by " + str(self.user)

class SubComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.TextField(max_length = 500)
    time = models.DateTimeField()

    def __str__(self):
       return "Subcomment from " +  str(self.user) + " on " + str(self.comment.article.name) + " article"  


    
