from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import SleepingBags, Participant, StatusChoice
from django.utils import timezone
from SleepingBag.forms import SleepingBagsForm
from SleepingBag.models import SleepingBags
from Location.models import Location
from django.contrib.auth.decorators import login_required


# Create your views here.
# user stories
# Cameron is an admin and has access ot the dashboard
# Should there be a staff role ? => need to be able to activate pending employees?
# As an new employee I need to be able to register
#/ register, registration form BUT you will get a pending status
# As an employee I need to be able to create a note
# As an employee I need to be able to registered in bulk sleeping bags

# missing the flow for cleaning a sleeping bag
# As an employee I need to be able to receive a allocated and put it as in stock
# As an employee I need to be able to give back an allocated sleeping bag
# As an employee to be able to do a swap easily

# Receive form, entr the name the particpant,


# Swap the sleeping bag view
from django.utils.decorators import async_only_middleware



# the following is not yet save/secured doesnt require logged in
def swap_sleeping_bag(request, participant_id):
    # Check if the request is AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest': # Check if the request is AJAX
        try:
            participant = get_object_or_404(Participant, pk=participant_id)
            # a swap, we have a clean sleeping bag in the facility attache to the participant
            clean_bag = SleepingBags.objects.filter(linked_participant=participant, is_washed=True, is_in_facility=True).first()
            dirty_bag = SleepingBags.objects.filter(linked_participant=participant, is_in_facility=False).first()

            if clean_bag and dirty_bag:
                # Process the swap
                dirty_bag.is_in_facility = True
                dirty_bag.is_washed = False
                dirty_bag.save()

                clean_bag.is_in_facility = False
                clean_bag.is_washed = False 
                clean_bag.save()
                print('there befor return true')
                return JsonResponse({"success": True, "message": "De Slaapzakken zijn succesvol omgeruild"})
            else:
                return JsonResponse({"success": False, "message": "Het omruilen is niet gelukt"})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    return HttpResponse("This endpoint requires an AJAX request.", status=400)


def report_lost_bag(request, bag_id):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            bag_to_report = get_object_or_404(SleepingBags, pk=bag_id)
            
            if bag_to_report.status == StatusChoice.LOST:
                return JsonResponse({"success": False, "message": "This bag is already reported as lost."})
            
            bag_to_report.status = StatusChoice.LOST
            bag_to_report.save()
            return JsonResponse({"success": True, "message": "The bag has been reported lost."})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    return HttpResponse("This endpoint requires an AJAX request.", status=400)

# View for washing now
def wash_now(request, bag_id):
    if request.method == 'POST':
        try:
            bag_to_wash = get_object_or_404(SleepingBags, pk=bag_id)
            bag_to_wash.is_washed = True
            bag_to_wash.last_washing_cycle = timezone.now().date()
            bag_to_wash.save()
            return JsonResponse({"success": True, "message": "The bag has been washed."})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    return HttpResponse("This endpoint requires a POST request.", status=400)

# View for upudating the bag

def update_bag(request, bag_id):       
    if request.method=="POST":
        bag= SleepingBags.objects.get(id=bag_id)
        form = SleepingBagsForm(request.POST, instance=bag)            
        if form.is_valid():                
            form.save()                        
            return redirect('participants:participant_details', id=bag.linked_participant.pk)
        else:
            print("rerrors", form.errors)
    return HttpResponse("This endpoint requires a POST request.", status=400)

# Our available stock of sleeping bags

from django.shortcuts import render, get_object_or_404
from .models import SleepingBags
from Location.models import Location
from Employee.models import Employee

@login_required
def stock(request, location_id):
    employee = Employee.objects.get(user=request.user)
    location = get_object_or_404(Location, id=location_id)
    if location != employee.location:
        return HttpResponse("You do not have permission to view this location's stock.", status=403)
    
    available_bags = SleepingBags.objects.filter(location=location, linked_participant__isnull=True)

    context = {
        'location': location,
        'available_bags': available_bags,
    }
    return render(request, 'SleepingBag/stock.html', context)