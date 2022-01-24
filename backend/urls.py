"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import (path, include, )
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf import settings

from backend.base import BASE_URL
BASE_URL=settings.BASE_URL





urlpatterns = [
    
    path(BASE_URL+'api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(BASE_URL+'api/doc/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path(BASE_URL+'api/redoc/', SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),
    
    path(BASE_URL+'admin/', admin.site.urls),
    path(BASE_URL+'api/auth', include('authentication.urls'))
    
]
handler404 = 'backend.views.error404'
handler500 = 'rest_framework.exceptions.server_error'
handler400 = 'rest_framework.exceptions.bad_request'
# handler403 = 'rest_framework.exceptions.bad'
