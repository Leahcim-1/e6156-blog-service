from django.db import models

# Create your models here.


class Test(models.Model):
  name = models.CharField(max_length=100, blank=True, default='')
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
        ordering = ['created']


class Blog2(models.Model):
  title =  models.CharField(unique=True, max_length=50, blank=False)
  body = models.TextField()
  user_id = models.IntegerField(default=000)
  tag = models.CharField(max_length=50,default='NAN')
  create_time = models.DateTimeField(auto_now_add=True)
  update_time = models.DateTimeField(auto_now=True)