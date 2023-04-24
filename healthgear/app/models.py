from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.utils.deprecation import MiddlewareMixin
import os
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    followers = models.ManyToManyField(User,related_name="followers",blank=True)
    followings = models.ManyToManyField(User,related_name="followings",blank=True)
    profile_picture = models.ImageField( upload_to='profilepics')

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="posts")
    description = models.CharField(max_length=200, default="GFG is best",blank=True,null=True)
    likes = models.ManyToManyField(User,related_name='likes',blank=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

class Uploadworkoutvideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to='workoutpost', validators = [FileExtensionValidator(allowed_extensions=['mp4'])])
    titleofvideo = models.TextField()
    dietdescription = models.TextField()
    country = models.CharField(max_length=100)
    day = models.CharField(max_length=250)
    muscle = models.CharField(max_length=100)
    ping = models.ManyToManyField(User, related_name='ping', blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    viewss = models.IntegerField(null=True,blank=True,default=0)

    def get_absolute_url(self):
        return reverse("viewactualgallery", kwargs={"pk": self.pk})

class Bodyweight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bodyvideo =  models.FileField(upload_to='bodyworkoutpost', validators = [FileExtensionValidator(allowed_extensions=['mp4'])])
    title = models.TextField()
    bodylikes = models.ManyToManyField(User, related_name='bodylikes', blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    viewss = models.IntegerField(null=True, blank=True, default=0)

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    remark = RichTextField()
    #imagey = models.ImageField(upload_to="blogposts")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Commentworkout(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    workoutpost = models.ForeignKey(Uploadworkoutvideo,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Recepies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recepievideo = models.FileField(upload_to='recepievideo', validators = [FileExtensionValidator(allowed_extensions=['mp4'])])
    recepietitle = models.CharField(max_length=200)
    instructions = models.CharField(max_length=200)
    preptime = models.CharField(max_length=200)
    cooktime = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    tools = models.CharField(max_length=200)
    viewss = models.IntegerField(null=True, blank=True, default=0)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)





