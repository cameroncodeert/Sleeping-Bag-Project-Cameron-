from django.db import models
from django.contrib.auth.models import User
from Location.models import Location



class Employee(models.Model):
    position = models.CharField(max_length=250, verbose_name="Rol medewerker")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True) 

    def __str__(self):
        return f"{self.user.first_name} - {self.position}"

    

