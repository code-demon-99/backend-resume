from django.db import models

# Create your models here.

class Experience  (models.Model):
  job_title=models.CharField(max_length=2000)
  job_desc = models.TextField()
  start = models.DateField()
  end = models.DateField(blank=True,null=True)
company= models.CharField(max_length=2000)   

   
