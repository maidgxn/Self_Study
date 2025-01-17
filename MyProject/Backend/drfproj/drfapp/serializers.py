from rest_framework import serializers
from .models import Hero

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = (
            'name', 'hero_name', 'quirk'
        )