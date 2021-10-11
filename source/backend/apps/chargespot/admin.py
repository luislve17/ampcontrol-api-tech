from django.contrib import admin

from .models import Chargespot

class ChargespotAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "lat", "lng", "last_maintenance_date")
    search_fields = ["id", "name", "lat", "lng", "last_maintenance_date"]
    fields = ("name", "lat", "lng", "last_maintenance_date")

admin.site.register(Chargespot, ChargespotAdmin)