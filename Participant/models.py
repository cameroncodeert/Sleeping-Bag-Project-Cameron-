from django.db import models
from Location.models import Location
# Create your models here.
class Participant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    registered_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
  # present in sql table
    # full_name = models.CharField(max_length=200)
# property not present in sql table, is computed on the fly
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name
   