from django.db import models

# Create your models here.

class Blog2(models.Model):
  title =  models.CharField(unique=True, max_length=50, blank=False)
  # subtitle
  body = models.TextField()
  user_id = models.IntegerField(default=000)
  # user_name
  tag = models.CharField(max_length=50,default='NAN')
  # Time format: Unix Timestamp
  create_time = models.DateTimeField(auto_now_add=True)
  update_time = models.DateTimeField(auto_now=True)