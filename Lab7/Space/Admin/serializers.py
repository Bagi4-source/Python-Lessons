from rest_framework import serializers
from .models import Moon, Planet, Star


class MoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moon
        fields = [
            'pk',
            'name',
            'planet_id',
        ]


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = [
            'pk',
            'name',
            'radius',
            'star_id',
        ]


class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = [
            'pk',
            'name',
            'mass',
        ]
