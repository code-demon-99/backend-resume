from django.shortcuts import render

# Create your views here.
from rest_framework import permissions

from .models import Experience
from .serializers import ExperienceSerializer
from rest_framework import viewsets


class ExperienceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows About details of a user  to be viewed or edited.
    """
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    # permission_classes = [permissions.IsAuthenticated]
