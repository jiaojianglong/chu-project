from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    type = models.IntegerField()# 1自己人  2游客
class Photo(models.Model):
    photo = models.CharField(max_length=256)
    dianzan = models.IntegerField(default=0)
    time = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
class Pinglun(models.Model):
    photo_id = models.ForeignKey('Photo')
    Pinglun_id = models.ForeignKey('Pinglun')
    user_id = models.ForeignKey('User')
    content = models.CharField(max_length=256)

class Video(models.Model):
    video = models.CharField(max_length=256)
    photo = models.CharField(max_length=256)
    dianzan = models.IntegerField(default=0)
    time = models.CharField(max_length=32)
    seenum = models.IntegerField(default=0)
    content = models.CharField(max_length=256)