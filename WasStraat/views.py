from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from Employee.models import Employee
from django.contrib.auth.models import User

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['position', 'location']

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_active=False
        if commit:
            user.save()
        return user



@login_required
def landing_page(request):
    return render(request, 'landing_page.html')

def login_user(request):
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
                    
        if user is not None:
            login(request, user)
        if User.objects.filter(username=username, is_active=False):
            return render(request, "login.html", context={"errors": "You are not yet activated"})
        return redirect('/')
    else:
        return render(request, "login.html")

from Participant.models import Participant
from Participant.forms import ParticipantForm


def register_user(request):
    if request.method == "POST":
        user_form = CustomUserCreationForm(request.POST)
        employee_form = EmployeeForm(request.POST)

        if user_form.is_valid() and employee_form.is_valid():
            print('hello world')
            user = user_form.save()
            employee = employee_form.save(commit=False)
            employee.user = user
            employee.save()

            login(request, user)
            return redirect('landing_page')

        else:
            return render(request, "register.html", {
                "user_form": user_form,
                "employee_form": employee_form,
                "errors": {**user_form.errors,  **employee_form.errors}
            })

    else:
        user_form = CustomUserCreationForm()
        employee_form = EmployeeForm()

    return render(request, "register.html", {
        "user_form": user_form,
        "employee_form": employee_form
    })



def logout_user(request):
    logout(request)
    return redirect('/login')
    