from django.shortcuts import render

# Create your views here.
from rest_framework import permissions

from api.projects.models import Project
from api.projects.serializers import ProjectSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows About details of a user  to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list (self,request):
        self.user = request.user
        print(self.user.id)
        self.queryset = ProjectSerializer.objects.get(user_id=self.user.id)
        return Response(ProjectSerializer(self.queryset).data)