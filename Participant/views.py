from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from Participant.models import Participant
from SleepingBag.models import SleepingBags
from .forms import ParticipantForm
from Employee.models import Employee
from django.contrib.auth.models import User
from Location.models import Location

# Create your views here.


@login_required
def dashboard_view(request):
    # Assuming your Employee model has a 'user' field that links to the Django User.
    employee = request.user.employee  # Make sure 'employee' field is accessible like this
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

     # debug
    print("Participant: ", participant.full_name)
    print("DOB: ", participant.date_of_birth)
    print("Sleeping Bags: ", list(sleeping_bags.values()))

    return render(request, 'Notes/participant_detail.html', {
        'participant': participant,
        'sleeping_bags': sleeping_bags
    })


#A view to ad d and remove participants
@login_required
def add_participant(request):
    if not request.user.employee.can_manage_participants:
        return redirect('landing_page')

    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
    else:
        form = ParticipantForm()

    return render(request, 'add_participant.html', {'form': form})

@login_required
def remove_participant(request, participant_id):
    if not request.user.employee.can_manage_participants:
        return redirect('landing_page')

    participant = get_object_or_404(Participant, id=participant_id)
    participant.delete()
    return redirect('landing_page')

