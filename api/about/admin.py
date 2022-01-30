from django.contrib import admin
from .models import About , Sociallinks
# Register your models here
class AboutAdmin(admin.ModelAdmin):
    pass

class SociallinksAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sociallinks,SociallinksAdmin)  
admin.site.register(About,AboutAdmin)


