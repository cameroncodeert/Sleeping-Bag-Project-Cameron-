from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse

from .models import SleepingBags, Participant, StatusChoice
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


import logging

logger = logging.getLogger(__name__)
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, HttpResponse

def swap_sleeping_bag(request, participant_id):
    # Check if the request is AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            participant = get_object_or_404(Participant, pk=participant_id)
            current_location = participant.registered_location
            clean_bag = SleepingBags.objects.filter(location=current_location, is_washed=True, is_in_facility=True).first()
            dirty_bag = SleepingBags.objects.filter(linked_participant=participant, is_in_facility=False).first()

            if clean_bag and dirty_bag:
                # Process the swap
                dirty_bag.is_in_facility = True
                dirty_bag.is_washed = False
                dirty_bag.save()

                clean_bag.is_in_facility = False
                clean_bag.is_washed = False # Slaapzak moet gewassen worden wanneer deze is uitgedeeld
                clean_bag.save()

                return JsonResponse({"success": True, "message": "De Slaapzakken zijn succesvol omgeruild"})
            else:
                return JsonResponse({"success": False, "message": "No clean or dirty sleeping bags available for swapping."})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    return HttpResponse("This endpoint requires an AJAX request.", status=400)




from django.http import HttpResponse

def success_view(request):
    # Here you could render a template or just return a simple HttpResponse
    return HttpResponse("Swap successful!")

logger = logging.getLogger(__name__)

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

# def return_dirty_bag(request, participant_id):
#     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#         try:
#             participant = get_object_or_404(Participant, pk=participant_id)
#             dirty_bag = SleepingBags.objects.filter(linked_participant=participant, is_in_facility=False).first()

#             if dirty_bag:
#                 dirty_bag.is_in_facility = True
#                 dirty_bag.is_washed = False
#                 dirty_bag.save()
#                 return JsonResponse({"success": True, "message": "The dirty bag has been returned for washing."})
#             else:
#                 return JsonResponse({"success": False, "message": "No dirty bags found to return."})
#         except Exception as e:
#             return JsonResponse({"success": False, "message": str(e)})
#     return HttpResponse("This endpoint requires an AJAX request.", status=400)

# def success_view(request):
#     return HttpResponse("Action successful!")