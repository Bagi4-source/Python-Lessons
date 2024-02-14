from django.contrib import admin
from .models import Planet, Moon, Star


# Register your models here.

@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_filter = ["radius", "star_id"]
    search_fields = ["name"]
    list_display = ["__str__", "name", "radius", "star_id"]


@admin.register(Moon)
class MoonAdmin(admin.ModelAdmin):
    list_filter = ["planet_id"]
    search_fields = ["name"]
    list_display = ["__str__", "name", "planet_id"]


@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    list_filter = ["mass"]
    search_fields = ["name"]
    list_display = ["__str__", "name", "mass"]
