from django.db import models

from django.contrib.auth import get_user_model
# Create your models here.
USER = get_user_model()


# Create your models here.

class Skill(models.Model):
  name=models.CharField(max_length=300)
  points=models.FloatField()
  user_id = models.ForeignKey(USER,on_delete=models.CASCADE)

  def retrieve(self, request, pk=None):
      self.user = request.user
      self.queryset = Skill.objects.filter(user_id=self.user)
