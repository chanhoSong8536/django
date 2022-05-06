from django.db import models
from acc.models import User
# Create your models here.
class Book(models.Model):
    site_name = models.CharField(max_length=100)
    maker = models.ForeignKey(User, on_delete=models.CASCADE)
    site_url = models.TextField()
    site_con = models.TextField()
    impo = models.BooleanField()

    def __str__(self):
        return self.site_name