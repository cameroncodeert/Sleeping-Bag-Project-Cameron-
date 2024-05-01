from django.shortcuts import render
from django import forms
from django.forms import ModelForm
from .models import Note
# Create your views here.

#class NoteForm(forms.Form): 
#     #textfield doesnt work although i use it in models.py
#     # Field here are input field not model field
#     note = forms.CharField(label= 'The note about the participant', max_length=500)
#     participant = form

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["note","participant"]

#view function

def helloNote(request):
    if request.method=='POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            # note = form.cleaned_data['note']
            # partica
            # new_note = Note(note=note)
            # new_note.save()
    # filter new_notes to only return notes WITH a participant
    new_notes = Note.objects.filter(participant__isnull=False)
    #new_notes= Note.objects.exclude(participant__is_null)True)
    print(new_notes)
    form = NoteForm()
    context = {"new_notes": new_notes, 'form':form}
    return render(request, "Notes/index.html", context)
