from pyexpat import model
from django.db import models

# Create your models here.

class Skill(models.Model):
  name=models.CharField(max_length=300)
  points=models.FloatField()
  