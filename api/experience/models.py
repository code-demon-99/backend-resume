from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
USER = get_user_model()


# Create your models here.

class Experience  (models.Model):
  job_title=models.CharField(max_length=2000)
  job_desc = models.TextField()
  start = models.DateField()
  end = models.DateField(blank=True,null=True)
  company= models.CharField(max_length=2000)  
  user_id = models.ForeignKey(USER,on_delete=models.CASCADE) 
  

   
