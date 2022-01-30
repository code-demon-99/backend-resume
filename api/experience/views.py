from django.shortcuts import render

# Create your views here.
from rest_framework import permissions

from .models import Experience
from rest_framework.response import Response
from .serializers import ExperienceSerializer
from rest_framework import viewsets


class ExperienceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows About details of a user  to be viewed or edited.
    """
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        self.user = request.user
        print(self.user.id)
        self.queryset = Experience.objects.get(user_id=self.user.id)
        return Response(ExperienceSerializer(self.queryset).data)
