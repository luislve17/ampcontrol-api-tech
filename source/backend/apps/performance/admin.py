from django.contrib import admin

from .models import Weight

class WeightAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'vehicle_performance_weight', 'lat', 'lng')
    search_fields = ["id", 'name', 'vehicle_performance_weight', 'lat', 'lng']
    fields = ('name', 'vehicle_performance_weight', 'lat', 'lng')

admin.site.register(Weight, WeightAdmin)
