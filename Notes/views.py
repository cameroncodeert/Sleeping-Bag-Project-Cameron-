from django.shortcuts import render
#from django import forms
from django.forms import ModelForm
from .models import Note
from Employee.models import Employee
from django.contrib.auth.decorators import login_required
 
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
#change name below still to do 
@login_required
def manage_note(request):
    # check if the user is authenticated
    employee = Employee.objects.get(user=request.user)
    if request.method=='POST':          
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)          
            note.employee = employee
            note.save()
    # selct where first_condition AND second condition
    # 1) get the employee currently logged in 
    # print('employee location', type(employee.location))

    # filter new_notes to only return notes WITH a participant AND that are from the user location
    new_notes = Note.objects.filter(participant__isnull=False)
    new_notes = new_notes.filter(participant__registered_location= employee.location)

    #new_notes= Note.objects.exclude(participant__is_null)True)
    print(new_notes)
    form = NoteForm()
    context = {"new_notes": new_notes, 'form':form}
    return render(request, "Notes/index.html", context)


        # Return an 'invalid login' error message.


# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = Employee
#         fields = ["username", "email", "password"]

# def register_user(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save() 
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             #todo