from django.shortcuts import render
from .models import Note
from Employee.models import Employee
from .forms import NoteForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
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
        form = NoteForm(request.POST)
        print('referrer',referer)
        # print('next url', next_url)
        if form.is_valid():
            print('is vlai')
            note = form.save(commit=False)          
            note.employee = employee
            note.save()
            if referer:
                redirect(referer)

    # selct where first_condition AND second condition
    # 1) get the employee currently logged in 
    # print('employee location', type(employee.location))

    # filter new_notes to only return notes WITH a participant AND that are from the user location
    new_notes = Note.objects.filter(participant__isnull=False)
    new_notes = new_notes.filter(participant__registered_location= employee.location)
    
    #reversed list
    display_notes = list(new_notes)[::-1]

    #new_notes= Note.objects.exclude(participant__is_null)True)
    form = NoteForm()
    context = {"new_notes": display_notes, 'form':form}
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