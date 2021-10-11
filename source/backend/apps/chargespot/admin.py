from django.contrib import admin

from .models import Chargespot

class ChargespotAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location_hash", "last_maintenance_date")
    search_fields = ["id", "name", "location_hash", "last_maintenance_date"]
    fields = ("name", "location_hash", "last_maintenance_date")

admin.site.register(Chargespot, ChargespotAdmin)