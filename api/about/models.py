
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
USER =get_user_model()

class About(models.Model):
  name = models.CharField(max_length=500)
  # image=models.ImageField
  about = models.TextField()
  photo = models.ImageField(upload_to='about')
  user_id = models.OneToOneField(USER,on_delete=models.CASCADE,primary_key=True)
  
class Sociallinks(models.Model):
  name = models.CharField(max_length=100)
  url = models.URLField(max_length=5000)
  fa_icon = models.CharField(max_length=100)
  user_id = models.ForeignKey(USER,on_delete=models.CASCADE)
  
  
  