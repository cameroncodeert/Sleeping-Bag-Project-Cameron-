from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from Participant.models import Participant
from SleepingBag.models import SleepingBags
from .forms import ParticipantForm
from Employee.models import Employee
from django.contrib.auth.models import User
from Location.models import Location
from Notes.models import Note
from django.forms import ModelForm


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

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["note","participant"]

@login_required
def participant_detail(request, id):
    participant = get_object_or_404(Participant, pk=id)
    sleeping_bags = SleepingBags.objects.filter(linked_participant=participant)
    status_choices = SleepingBags._meta.get_field('status').choices

    
    employee = request.user.employee
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.employee = employee
            note.save()
    
    form = NoteForm()
    new_notes = Note.objects.filter(participant=participant)


    return render(request, 'Notes/participant_detail.html', {
        'participant': participant,
        'sleeping_bags': sleeping_bags,
        'status_choices': status_choices, 
        'form': form,
        'new_notes': new_notes
    })


#A view to ad d and remove participants
@login_required
def add_participant(request):
    if not request.user.employee.can_manage_participants:
        return redirect('landing_page')

    employee_location = request.user.employee.location

    if request.method == 'POST':
        form = ParticipantForm(request.POST, employee_location=employee_location)
        if form.is_valid():
            participant = form.save()
            # Assign the first sleeping bag
            sleeping_bag_1 = form.cleaned_data['sleeping_bag_1']
            if sleeping_bag_1:
                sleeping_bag_1.linked_participant = participant
                sleeping_bag_1.is_in_facility = False
                sleeping_bag_1.save()

            # Assign the second sleeping bag
            sleeping_bag_2 = form.cleaned_data['sleeping_bag_2']
            if sleeping_bag_2:
                sleeping_bag_2.linked_participant = participant
                sleeping_bag_2.is_in_facility = False
                sleeping_bag_2.save()

            return redirect('landing_page')
    else:
        form = ParticipantForm(employee_location=employee_location)

    available_sleeping_bags = SleepingBags.objects.filter(
        location=employee_location,
        linked_participant__isnull=True,
        is_in_facility=True
    )

    return render(request, 'add_participant.html', {
        'form': form,
        'available_sleeping_bags': available_sleeping_bags
    })
@login_required
def remove_participant(request, participant_id):
    if not request.user.employee.can_manage_participants:
        return redirect('landing_page')

    participant = get_object_or_404(Participant, id=participant_id)

    # When a user is deleted --> it resets their sleepingbags. 
    SleepingBags.objects.filter(linked_participant=participant).update(linked_participant=None, is_in_facility=True)

    participant.delete()
    return redirect('landing_page')

