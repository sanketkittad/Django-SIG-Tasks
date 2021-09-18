from django.db import models
from django.contrib.auth.models import User

class user2(models.Model):
    age=models.IntegerField()
    gender=models.CharField(max_length=6)
    phonenum=models.CharField(max_length=10)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
# Create your models here.
