from django.db import models
from Participant.models import Participant
from Employee.models import Employee
# Create your models here.
class Note(models.Model):
    #UserID
    note = models.TextField(max_length=500)
    # automatically the date field when the instance
    # auto_now will update the date everytime the instance is saved (last_time_updated)
    date = models.DateTimeField(auto_now_add=True)
    participant = models.ForeignKey(Participant,on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    #EmployeeID foreigkey 

    def __str__(self):
        if self.participant:
            return f"Bericht betreffend: {self.participant.full_name} Gemaakt op {self.date}"
        else:
            return "Bericht zonder gebruiker"

        #return  "A note about " + self.participant.full_name + " Created at " + str(self.date)


#notes = Notes.objects.all()

#{{note}} = {{note.str}} = 'A note about .......'
# shell python manage.py shell
# from Notes.models import Note
# NOte(note="helowolrdl")