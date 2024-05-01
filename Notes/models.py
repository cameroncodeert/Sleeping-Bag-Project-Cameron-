from django.db import models
from Participant.models import Participant
# Create your models here.
class Note(models.Model):
    #UserID
    note = models.TextField(max_length=500)
    # automatically the date field when the instance
    # auto_now will update the date everytime the instance is saved (last_time_updated)
    date = models.DateField(auto_now_add=True)
    participant = models.ForeignKey(Participant,on_delete=models.SET_NULL, null=True)
    #EmployeeID

    def __str__(self):
        # return self.note[:50]  #[] Return first 50 characters of the note
        # TODO : REFACTOR  using f-string
        # return f'A note about {self.particpatn.}
        return  "A note about " + self.participant.full_name + " Created at " + str(self.date)


#notes = Notes.objects.all()

#{{note}} = {{note.str}} = 'A note about .......'
# shell python manage.py shell
# from Notes.models import Note
# NOte(note="helowolrdl")