from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

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
    bio = models.TextField(max_length=500)
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

def upload_location(instance):
    return "articles/" +  str(instance.id)

ENGINE_CHOICES = (
    ("UNITY", "Unity Engine"),
    ("CRY", "Cry Engine"),
    ("UNREAL", "Unreal Engine"),
    ("OTHER", "Other Engines"),
)

VOTE_CHOICES = (
    ("UP","Upvote"),
    ("DOWN","Downvote"),
    ("NONE","NotVoted"),
)

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length = 50, default = "")
    engine = models.CharField(choices=ENGINE_CHOICES, max_length = 10)
    overview = models.TextField(max_length = 300, default = "")
    text = models.TextField(max_length = 10000, default = "")
    picture = models.ImageField(null=True, blank = True, width_field = 'pic_width', height_field = 'pic_height')
    pic_height = models.IntegerField(default = 0)
    pic_width = models.IntegerField(default = 0)
    verified = models.BooleanField()
    points = models.IntegerField(default = 0)
    released = models.BooleanField(default = False)
    tag = models.BooleanField(default = True)
    release_date = models.DateTimeField(default = datetime.datetime.now())

    def __str__(self):
       return "Article " + self.name + " by " + str(self.user) + " " + str(self.points) + " points, Engine: " + str(self.engine) 


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField(max_length = 500)
    time = models.DateTimeField(default = datetime.datetime.now())

    def __str__(self):
       return "Comment on article "+ str(self.article.name) + " by " + str(self.user)

class SubComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.TextField(max_length = 500)
    time = models.DateTimeField(default = datetime.datetime.now())

    def __str__(self):
       return "Subcomment from " +  str(self.user) + " on " + str(self.comment.article.name) + " article"  



    
