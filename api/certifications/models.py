from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()


# Create your models here.

class Certificate(models.Model):
  name=models.CharField( max_length=5000)
  issuing_organization  = models.CharField(max_length=5000)
  do_expire = models.BooleanField(default=False)
  issue_date = models.DateField()
  expiration_certificate = models.DateField( auto_now=False, auto_now_add=False)
  credential_ID =models.CharField( max_length=500)
  credential_url = models.URLField(max_length=1000)
  user_id = models.ForeignKey(USER,on_delete=models.CASCADE)
  