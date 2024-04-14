from rest_framework import serializers
from .models import SocialMediaSettings, SiteSettings

class SocialMediaSettingsSerializer(serializers.ModelSerializer):
	class Meta:
		model = SocialMediaSettings
		fields = '__all__'

class SiteSettingsSerializer(serializers.ModelSerializer):
	class Meta:
		model = SiteSettings
		fields = '__all__'
