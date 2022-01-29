from django.shortcuts import render

from api.about.models import About
from rest_framework import permissions
from .serializers import AboutSerializer
from rest_framework import viewsets


class AboutViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows About details of a user  to be viewed or edited.
    """
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    # permission_classes = [permissions.IsAuthenticated]

# Create your views here.
