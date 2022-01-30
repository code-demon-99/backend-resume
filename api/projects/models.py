from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
USER = get_user_model()


# Create your models here.
class Project(models.Model):
  name=models.CharField(max_length=500,unique=True)
  tech_stack = models.CharField(max_length=300)
  git_repo_link  = models.URLField(blank=True,null=True)
  project_link = models.URLField(blank=True,null=True)
  description=models.TextField(blank=True)
  tags = models.JSONField()
  user_id = models.ForeignKey(USER,on_delete=models.CASCADE)
  
  

  
  