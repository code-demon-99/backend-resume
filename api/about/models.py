from email.mime import image
from django.db import models

# Create your models here.

class About(models.Model):
  name = models.CharField(max_length=500)
  # image=models.ImageField
  about = models.TextField()
  photo = models.ImageField(upload_to='about')
  