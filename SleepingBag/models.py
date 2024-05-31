from django.db import models
from Location.models import Location
from Participant.models import Participant
from django.db.models import Case, When


class StatusChoice(models.TextChoices):
    GOOD = 'Good', 'Goed'
    DAMAGED = 'Damaged', 'Beschadigd'
    LOST = 'Lost', 'Verloren'

custom_ordering = Case(
    When(status=StatusChoice.GOOD, then=0),
    When(status=StatusChoice.DAMAGED, then=1),
    When(status=StatusChoice.LOST, then=2),
    default=3  # In case there's a status not defined in StatusChoice, put it at the end
)
# Enumeration for the sleepign bag status choices

class SleepingBags(models.Model):
    status = models.CharField(choices=StatusChoice.choices, max_length=10, verbose_name="Status")
    is_washed = models.BooleanField(default=True, verbose_name="Is gewassen")
    date_of_received = models.DateField(auto_now_add=True, verbose_name="Datum van ontvangst")
    # SET_NULL = if location is deleted, keep sleeping bags, CASCADE= if location is deleted, verwijder all sleeping bags with this location
    location = models.ForeignKey(Location, on_delete= models.SET_NULL, null=True)
    is_in_facility = models.BooleanField(default=True, verbose_name="Locatie")
    last_washing_cycle = models.DateField(auto_now=True,verbose_name="Laatst gewassen")
    linked_participant = models.ForeignKey(Participant, on_delete=models.SET_NULL, null=True, blank=True) 





