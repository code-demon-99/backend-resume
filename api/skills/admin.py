from django.contrib import admin
from .models import Skill


# Register your models here.
class SkillAdmin(admin.ModelAdmin):
  pass
admin.site.register(Skill,SkillAdmin)