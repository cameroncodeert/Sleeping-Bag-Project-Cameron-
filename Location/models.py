from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=250)
    max_capacity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)])
    address = models.CharField(max_length=250)
    

    def __str__(self):
        return self.name


# SELECT * FROM LOCATION WHERE ID=1
#location = Location.objects.get(id=1)
# location.name


#select * from Location
#locations = Location.objects.all()