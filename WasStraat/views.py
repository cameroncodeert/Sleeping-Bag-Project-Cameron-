from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from Employee.models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'position', 'location', 'can_manage_participants']


@login_required
def landing_page(request):
    return render(request, 'Notes/landing_page.html')

def login_user(request):
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:

            login(request, user)
        return redirect('/')
    else:
        return render(request, "Notes/login.html")

from Participant.models import Participant
from Participant.forms import ParticipantForm


def register_user(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        employee_form = EmployeeForm(request.POST)

        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save()
            employee = employee_form.save(commit=False)
            employee.user = user
            employee.save()

            login(request, user)
            return redirect('landing_page')

        else:
            return render(request, "Notes/register.html", {
                "user_form": user_form,
                "employee_form": employee_form,
                "errors": user_form.errors + employee_form.errors
            })

    else:
        user_form = UserCreationForm()
        employee_form = EmployeeForm()

    return render(request, "Notes/register.html", {
        "user_form": user_form,
        "employee_form": employee_form
    })



def logout_user(request):
    logout(request)
    return redirect('/login')
    