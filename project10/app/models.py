from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ImageField()

def __str__(self):
    return self.username.username
