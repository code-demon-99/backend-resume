from rest_framework import serializers
from .models import About , Sociallinks
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class SociallinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sociallinks
        fields = '__all__'
