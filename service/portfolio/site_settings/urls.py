from django.urls import path
from .views import SiteSettingsViewSet, SocialMediaSettingsViewSet

urlpatterns = [
    path("site-settings/", SiteSettingsViewSet.as_view({'get': 'list'})),
    path("social-media-settings/", SocialMediaSettingsViewSet.as_view({'get': 'list'})),
]