from distutils.command.upload import upload
from django.db import models
from acc.models import User
# Create your models here.

class Topic(models.Model):
    subject = models.CharField(max_length=100)
    maker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="maker")
    content = models.TextField()
    voter = models.ManyToManyField(User, blank=True, related_name="voter")
    pubdate = models. DateTimeField()

    def __str__(self):
        return self.subject

    def summary(self):
        if len(self.content) > 10:
            return f"{self.content[:10]}..."
        return self.content

class Choice(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="vote/%y/%m")
    con = models.TextField()
    choicer = models.ManyToManyField(User, blank=True) 

    def __str__(self):
        return f"{self.topic}_{self.name}"