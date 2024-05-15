from django.db import models
from django.contrib.auth.models import User
from Location.models import Location


# Define my Employee model with user details and location details

class Employee(models.Model):
    ROLE_CHOICES = [
            ('Beheerder', 'Beheerder'),
            ('Medewerker', 'Medewerker'),
            ('Vrijwilliger', 'Vrijwilliger'),
            ('Supervisor', 'Supervisor'),
            ('Coördinator', 'Coördinator'),
            ('Manager', 'Manager'),
            ('Directeur', 'Directeur'),
    ]
    position = models.CharField(max_length=250, choices=ROLE_CHOICES, verbose_name="Rol medewerker", default='Medewerker')
    user = models.OneToOneField(User, on_delete=models.CASCADE) #, related_name='employee')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True) 
    can_manage_participants = models.BooleanField(default=False)


    # A string representation for Employee
    def __str__(self):
        return f"{self.user.first_name} - {self.position}"
    
    def save(self, *args, **kwargs):
        if self.position == 'Beheerder' and not self.can_manage_participants:
            if Employee.objects.filter(location=self.location, can_manage_participants=True).exists():
                raise ValueError("Slechts de Beheerder op deze locatie kan deze actie uitvoeren.")
        super().save(*args, **kwargs)