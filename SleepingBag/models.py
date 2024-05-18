from django.db import models
from Location.models import Location
from Participant.models import Participant

# Enumeration for the sleepign bag status choices
class StatusChoice(models.TextChoices):
    GOOD = 'Good', 'Goed'
    DAMAGED = 'Damaged', 'Beschadigd'
    LOST = 'Lost', 'Verloren'
    BAD = 'Bad', 'Slecht'  


class SleepingBags(models.Model):
    status = models.CharField(choices=StatusChoice.choices, max_length=10)
    is_washed = models.BooleanField(default=True)
    date_of_received = models.DateField(auto_now_add=True)
    # SET_NULL = if location is deleted, keep sleeping bags, CASCADE= if location is deleted, verwijder all sleeping bags with this location
    location = models.ForeignKey(Location, on_delete= models.SET_NULL, null=True)
    is_in_facility = models.BooleanField(default=True)
    last_washing_cycle = models.DateField(auto_now=True)
    linked_participant = models.ForeignKey(Participant, on_delete=models.SET_NULL, null=True, blank=True) 





