from django.contrib import admin
from .models import Location
# Register your models here.
#  @ is a decorator => https://realpython.com/primer-on-python-decorators/
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'max_capacity', 'address')
