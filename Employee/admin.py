from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'location', 'position', 'can_manage_participants')

    def full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    full_name.short_description = 'Name'



