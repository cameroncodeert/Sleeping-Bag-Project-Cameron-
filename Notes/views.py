from django.shortcuts import render
from .models import Note
from Employee.models import Employee
from .forms import NoteForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
# Create your views here.

#class NoteForm(forms.Form): 
#     #textfield doesnt work although i use it in models.py
#     # Field here are input field not model field
#     note = forms.CharField(label= 'The note about the participant', max_length=500)
#     participant = form


#view function
#change name below still to do 
# list and add
@login_required
def manage_note(request):
  
    employee = Employee.objects.get(user=request.user)
    referer = request.META.get('HTTP_REFERER')
    if request.method=='POST':          
        # next_url = request.POST.get('next')
        # request.POST.remove('csrfmiddlewaretoken')
        form = NoteForm(request.POST)
        # print('referrer',referer)
        # print('next url', next_url)
        print("data", form.data)
        if form.is_valid():
            print('is valid')
            note = form.save(commit=False)          
            note.employee = employee
            note.save()
            if referer:
                
                return redirect(referer)
                # HttpResponseRedirect(referer)
        else:
            print('errors', form.errors)


    # filter new_notes to only return notes WITH a participant AND that are from the user location
    new_notes = Note.objects.filter(participant__isnull=False)
    new_notes = new_notes.filter(participant__registered_location= employee.location).order_by('-date')
    
    #reversed list
    # display_notes = list(new_notes)[::-1]
    display_notes= new_notes
    #new_notes= Note.objects.exclude(participant__is_null)True)
    form = NoteForm()
    context = {"new_notes": display_notes, 'form':form}
    return render(request, "index.html", context)


        # Return an 'invalid login' error message.


