from django.shortcuts import render

from api.about.models import About, Sociallinks
from rest_framework import permissions
from .serializers import AboutSerializer, SociallinksSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class  AboutViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows About details of a user  to be viewed or edited.
    """
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def list (self,request):
        self.user = request.user
        print(self.user.id)
        self.queryset = About.objects.get(user_id=self.user.id)
        return Response(AboutSerializer(self.queryset).data)
        

class SociallinksViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows About details of a user  to be viewed or edited.
    """
    queryset = Sociallinks.objects.all()
    serializer_class = SociallinksSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request):
        self.user = request.user
        print(self.user.id)
        self.queryset = Sociallinks.objects.get(user_id=self.user.id)
        return Response(SociallinksSerializer(self.queryset).data)


# Create your views here.
