from django.urls import include, path
from rest_framework import routers
from .authentication import views
from .about.views import  AboutViewSet , SociallinksViewset
from .experience.views import ExperienceViewSet
from .education.views import EducationViewSet
from .projects.views import ProjectViewSet
from .skills.views import SkillViewSet
from .certifications.views import CertificateViewSet

# DRF routing the urls 
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'about', AboutViewSet)
router.register(r'slinks', SociallinksViewset)
router.register(r'skills', SkillViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'edu', EducationViewSet)
router.register(r'exp', ExperienceViewSet)
router.register(r'cert', CertificateViewSet)





urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls')),
]
