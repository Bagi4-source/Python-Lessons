from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Moons', views.MoonView)
router.register('Planets', views.PlanetView)
router.register('Stars', views.StarView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
urlpatterns.extend(staticfiles_urlpatterns())