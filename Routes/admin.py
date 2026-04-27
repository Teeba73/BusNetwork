from django.contrib import admin
from .models import Station, Route

# Register your models here.
class RouteAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")
    list_filter = ("origin", "destination")
    filter_horizontal = ("passengers",)

admin.site.register(Station)
admin.site.register(Route, RouteAdmin)
