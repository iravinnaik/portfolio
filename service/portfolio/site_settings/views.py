from django.shortcuts import render
from rest_framework import viewsets
from .models import SocialMediaSettings, SiteSettings
from .serializers import SocialMediaSettingsSerializer, SiteSettingsSerializer
from rest_framework.response import Response

# Create your views here.
class SocialMediaSettingsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = SocialMediaSettings.objects.all()
        serializer = SocialMediaSettingsSerializer(queryset, many=True)
        return Response(serializer.data)
    

class SiteSettingsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = SiteSettings.objects.all()
        serializer = SiteSettingsSerializer(queryset, many=True)
        return Response(serializer.data)