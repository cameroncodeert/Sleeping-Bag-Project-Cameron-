from django.contrib import admin
from .models import SleepingBags
# Register your models here.
@admin.register(SleepingBags)

class SleepingBagsAdmin(admin.ModelAdmin):
    list_display = ("status","location","id")

