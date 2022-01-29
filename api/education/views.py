from django.shortcuts import render

# Create your views here.
from rest_framework import permissions

from .models import Education
from .serializers import EducationSerializer
from rest_framework import viewsets


class EducationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows About details of a user  to be viewed or edited.
    """
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    # permission_classes = [permissions.IsAuthenticated]
