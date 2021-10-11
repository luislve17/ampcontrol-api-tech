from django.contrib import admin

from .models import Vehicle

class VehicleAdmin(admin.ModelAdmin):
    list_display = ("id", "brand", "owner", "battery_installation_date")
    search_fields = ["id", "brand", "owner", "battery_installation_date"]
    fields = ("brand", "owner", "battery_installation_date")

admin.site.register(Vehicle, VehicleAdmin)