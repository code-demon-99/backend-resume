import imp
from django.shortcuts import render
from . serializers import SkillSerializer
from .models import Skill
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.


class SkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows About details of a user  to be viewed or edited.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticated ]
    
    def list(self, request):
        self.user = request.user
        print(self.user.id)
        self.queryset = Skill.objects.get(user_id=self.user.id)
        return Response(SkillSerializer(self.queryset).data)

# Create your views here.
