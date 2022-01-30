from tracemalloc import start
from django.db import models

from django.contrib.auth import get_user_model
# Create your models here.
USER = get_user_model()


# Create your models here.
class Education(models.Model):
  institute_name = models.CharField(max_length=2000)
  course_name =models.CharField(max_length=2000)
  start =models.DateField()
  End = models.DateField(blank=True,null=True)
  is_present = models.BooleanField(default=False)
  accomplishments = models.JSONField()
  obt_marks = models.CharField(max_length=5)
  user_id = models.ForeignKey(USER,on_delete=models.CASCADE)  
    