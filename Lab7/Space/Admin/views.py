from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Moon, Star, Planet
from .serializers import MoonSerializer, PlanetSerializer, StarSerializer


class MoonView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
               mixins.DestroyModelMixin, mixins.CreateModelMixin):
    queryset = Moon.objects.all()
    serializer_class = MoonSerializer


class StarView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
               mixins.DestroyModelMixin, mixins.CreateModelMixin):
    queryset = Star.objects.all()
    serializer_class = StarSerializer


class PlanetView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin, mixins.CreateModelMixin):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
