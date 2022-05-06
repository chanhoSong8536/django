from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pic = models.ImageField(upload_to="user/%y/%m")
    age = models.IntegerField(default=1)
    comment = models.TextField()
    
    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/user/noimage.png"