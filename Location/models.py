from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# My model to represent a physical location

class Location(models.Model):
    name = models.CharField(max_length=250)
    max_capacity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)])
    address = models.CharField(max_length=250)
    
    # String representation for Location
    def __str__(self):
        return self.name


