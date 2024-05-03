from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from Employee.models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['position', "location"]


@login_required
def landing_page(request):
#    if not request.user.is_authenticated:
#            return ('redirect_url')
    return render(request, 'Notes/landing_page.html')

def login_user(request):
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # user = User.objects.get(username=username, password=password)
        if user is not None:

            login(request, user)
        # Redirect to a success page.
        return redirect('/note')
    else:
        return render(request, "Notes/login.html")


def register_user(request):
    if request.method=="POST":
        # create everything
        print(request.POST)
        user_form = UserCreationForm(request.POST)
        employee_form = EmployeeForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
        else:
            print(user_form.errors)
            return render(request, "Notes/register.html", context= {"user_form":user_form, "employee_form":employee_form, "errors":user_form.error_class})
        if user and employee_form.is_valid():
            employee = employee_form.save(commit=False)
            employee.user = user
            employee.save()
        if user is not None:
            login(request, user)
            
        return redirect('/')
        
    employee_form = EmployeeForm()
    user_form = UserCreationForm()
    context = {'employee_form':employee_form, "user_form":user_form}
    return render(request, "Notes/register.html", context=context)

# Write the logout view
def logout_user(request):
    logout(request)
    return redirect('/login')
    