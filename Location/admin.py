from django.contrib import admin
from .models import Location

# Admin interface  for Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'max_capacity', 'address')
