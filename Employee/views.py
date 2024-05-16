from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeForm
from Participant.models import Participant
from SleepingBag.models import SleepingBags
from Participant.forms import ParticipantForm
from django.contrib.auth.models import User
from Location.models import Location

# Form to manage Employee data

# class EmployeeForm(ModelForm):
#     class Meta:
#         model = Employee
#         fields = ["name", "position", 'can_manage_participants']

# A view to handle Employee creation and updates
def manageEmployee(request):
    if request.method=='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page') 
    else:
        form = EmployeeForm()
    return render(request, 'manage_employee.html', {'form': form})

@login_required
def dashboard_view(request):
    employee = request.user.employee  
    participants = Participant.objects.filter(registered_location=employee.location)
    participant_data = []

    for participant in participants:
        sleeping_bags = SleepingBags.objects.filter(linked_participant=participant)
        participant_data.append({
            'participant': participant,
            'sleeping_bags': sleeping_bags
        })

    context = {
        'employee': employee,
        'participant_data': participant_data
    }
    return render(request, 'Notes/landing_page.html', context)

@login_required
def participant_detail(request, id):
    participant = get_object_or_404(Participant, pk=id)
    sleeping_bags = SleepingBags.objects.filter(linked_participant=participant)

    return render(request, 'Notes/participant_detail.html', {
        'participant': participant,
        'sleeping_bags': sleeping_bags
    })


# @login_required
# def remove_participant(request, participant_id):
#     if not request.user.employee.can_manage_participants:
#         return redirect('landing_page')

#     participant = get_object_or_404(Participant, id=participant_id)
#     participant.delete()
#     return redirect('landing_page')
    



