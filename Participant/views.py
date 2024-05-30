from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Participant.models import Participant
from SleepingBag.models import SleepingBags
from .forms import ParticipantForm
from Employee.models import Employee
from django.contrib.auth.models import User
from Location.models import Location
from Notes.models import Note
from django.forms import ModelForm
from django.urls import reverse
from django.http import HttpResponseRedirect
# from Notes.views import NoteForm
from Notes.forms import NoteFormHiddenParticipant as NoteForm
from SleepingBag.forms import SleepingBagsForm, SleepingBagsCustomForm 



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

    unwashed_bags = SleepingBags.objects.filter(
        location=employee.location,
        is_washed=False
    ).select_related('linked_participant')


    print("Employee:", employee)
    print("Location:", employee.location)
    print("Unwashed Bags:", unwashed_bags)
    
    for bag in unwashed_bags:
        print(f"Bag ID: {bag.id}, Participant: {bag.linked_participant}, Status: {bag.status}, Location: {bag.location}")

    context = {
        'employee': employee,
        'participant_data': participant_data,
        'unwashed_bags': unwashed_bags  
    }
    return render(request, 'Notes/landing_page.html', context)

@login_required
def participant_detail(request, id):
    participant = get_object_or_404(Participant, pk=id)
    sleeping_bags = SleepingBags.objects.filter(linked_participant=participant).order_by('-is_washed')
    bags_forms = [SleepingBagsForm(instance=sleeping_bag) for sleeping_bag in sleeping_bags]
    bags_forms_ext = zip(sleeping_bags, bags_forms)

    employee = request.user.employee
    if request.method == 'POST':
        form = NoteForm(request.POST, participant=participant)
        if form.is_valid():
            note = form.save(commit=False)
            note.employee = employee
            note.save()
            return HttpResponseRedirect(reverse('participant_detail', args=[id]))  # Redirect to clear the form
    else:
        note_form = NoteForm(participant= participant) 

    new_notes = Note.objects.filter(participant=participant).order_by('-date')  # Order notes by date

    context = {
        'participant': participant,
        'sleeping_bags': sleeping_bags,
        'note_form': note_form,
        'new_notes': new_notes,
        'bags_forms_ext': bags_forms_ext
    }

    # Add 'my_form' to context only if 'bags_forms' is not empty so that we can also click on Participants
    #without any sleeping bags assigned
    if bags_forms:
        context['my_form'] = bags_forms[0]

    return render(request, 'Participant/participant_detail.html', context)


from .forms import ParticipantForm2
@login_required
def add_participant(request):
    if not request.user.employee.can_manage_participants:
        return redirect('landing_page')

    employee_location = request.user.employee.location
    available_sleeping_bags = SleepingBags.objects.filter(
        location=employee_location,
        linked_participant__isnull=True,
        is_in_facility=True
    )
    if request.method == 'POST':
        form = ParticipantForm2(request.POST, employee_location=employee_location)
        print("form", form)
        if form.is_valid():
            print('is valide')
            participant = form.save()
            # participant.is_active = True

            # if form.cleaned_data['document_type'] == 'other':
            #     participant.document_type = form.cleaned_data['custom_document_type']
            # participant.save()

            # Assign thve first sleeping bag
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
            messages.success(request, 'Deelnemer succesvol toegevoegd!')
            return HttpResponseRedirect(reverse('participants:add_participant')) 
        else:
            # print('errors',form.errors)

           render(request, 'Participant/add_participant.html', {
        'form': form,
        "errors": form.errors,
        'available_sleeping_bags': available_sleeping_bags,
        'employee_location_name': request.user.employee.location.name,
    })
    else:
        form = ParticipantForm2(employee_location=employee_location)

    

    return render(request, 'Participant/add_participant.html', {
        'form': form,
        'available_sleeping_bags': available_sleeping_bags,
        'employee_location_name': request.user.employee.location.name,
    })

@login_required
def remove_participant(request, participant_id):
    if not request.user.employee.can_manage_participants:
        return redirect('landing_page')

    participant = get_object_or_404(Participant, id=participant_id)
    
    # When a user is deleted --> it resets their sleepingbags. 
    SleepingBags.objects.filter(linked_participant=participant).update(linked_participant=None, is_in_facility=True)
    
    participant.is_active = False  # Now mark the participant as inactive
    participant.save()
    
    return redirect('landing_page')


