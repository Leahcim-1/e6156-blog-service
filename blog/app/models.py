from django.db import models
from unixtimestampfield.fields import UnixTimeStampField


# Create your models here.

class Blog2(models.Model):
  title =  models.CharField(unique=True, max_length=50, blank=False) 
  subtitle =  models.CharField(unique=False, max_length=100, blank=True)
  body = models.TextField()
  user_id = models.IntegerField(unique=False, default=000)
  user_name =  models.CharField(unique=False, max_length=20, blank=True)
  tag = models.CharField(max_length=50,default='NAN')
  # Time format: Unix Timestamp
  create_time = models.DateTimeField(auto_now_add=True)
  update_time = models.DateTimeField(auto_now=True)