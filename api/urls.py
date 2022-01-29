from .about.views import  AboutViewSet
from .experience.views import ExperienceViewSet
from .education.views import EducationViewSet
from .projects.views import ProjectViewSet
from .skills.views import SkillViewSet
from rest_framework import routers
from django.urls import include, path
from .authentication import views




# DRF routing the urls 
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'about', AboutViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'edu', EducationViewSet)
router.register(r'exp', ExperienceViewSet)





urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls')),
]
