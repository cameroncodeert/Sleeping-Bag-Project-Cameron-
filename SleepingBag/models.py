from django.db import models
from Location.models import Location
# Create your models here.
# enumeration how it looks, how it saved or used by a dev
class StatusChoice(models.TextChoices):
    Good = ('Good', 'Good')
    Bad = ('Bad', 'Bad')

class SleepingBags(models.Model):
    status = models.CharField(choices=StatusChoice.choices, max_length=4)
    is_washed = models.BooleanField(default=True)
    date_of_received = models.DateField(auto_now_add=True)
    # SET_NULL = if location is deleted, keep sleeping bags, CASCADE= if location is deleted, delete all sleeping bags with this location
    # one to one
    location = models.ForeignKey(Location, on_delete= models.SET_NULL, null=True)
    # locations = models.ManyToManyField
    # models.ManyToManyField
    is_in_facility = models.BooleanField(default=True)
    last_washing_cycle = models.DateField(auto_now=True)



#python def for to update last_washing cycle 
