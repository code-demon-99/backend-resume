from django.shortcuts import render

# Create your views here.
from .serializers import CertificateSerializer
from .models import Certificate
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response

class CertificateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows About details of a user  to be viewed or edited.
    """
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        self.user = request.user
        print(self.user.id)
        self.queryset = Certificate.objects.get(user_id=self.user.id)
        return Response(CertificateSerializer(self.queryset).data)
