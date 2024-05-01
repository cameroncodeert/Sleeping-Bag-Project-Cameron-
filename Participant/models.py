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
    # def save(self, *args, **kwargs):
    #     self.full_name = self.first_name + " " + self.last_name
    #     super().save(*args, **kwargs)
#  participatn = Particpant(first_name='kevin', last_name="morivllier")
#  participatn.save()
#  participatn.full_name
#  kevin morvillier
# participant is an record (instance)
# participant.registed_location => id of the location
# location = Location.objects.get(id= participant.registered_location)
# location.max_capacity
# participant.registered_location.adress => instance of the location 