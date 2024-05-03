from django.shortcuts import render
from django.forms import ModelForm
from .models import Employee
# Create your views here.


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["name", "position"]

#function

def manageEmployee(request):
    if request.method=='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
#notdone
    



