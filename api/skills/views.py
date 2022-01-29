import imp
from django.shortcuts import render
from . serializers import SkillSerializer
from .models import Skill
from rest_framework import permissions
from rest_framework import viewsets

# Create your views here.


class SkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows About details of a user  to be viewed or edited.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    # permission_classes = [permissions.IsAuthenticated]

# Create your views here.
