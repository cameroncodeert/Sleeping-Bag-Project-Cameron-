from django.contrib import admin
from .models import Note
# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('note','date', 'location', "participant", "employee_name")

    def location(self, obj):
        if obj.participant:
            return obj.participant.registered_location
        return ''

    def employee_name(self,obj):
        if obj.employee:
            return obj.employee.user.first_name
        return ""

