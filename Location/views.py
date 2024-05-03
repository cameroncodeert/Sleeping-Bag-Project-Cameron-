import datetime
from django.shortcuts import render
#from django import forms
from .models import Location
from django.forms import ModelForm

# class LocationForm(forms.Form):
#     name = forms.CharField(label='The name of the location', max_length=250)
#     address = forms.CharField(label='The address of the location', max_length=250)
#     max_capacity = forms.IntegerField(label='The max capacity of the location')

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'address', 'max_capacity']

# class NoteForm(ModelForm):
#     class Meta:
#         model = Note
#         fields = ["note","participant"]
# Create your views here.

# view function
#/location/3
#/location/;DROP DATABASE;
def manageLocation(request):
    if request.method== "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            max_capacity = form.cleaned_data['max_capacity']
            location = Location(name=name, address=address, max_capacity=max_capacity)
            location.save()

        # manage everything post
        # create a new location 
        # sanit
    locations = Location.objects.all()
    form = LocationForm()
    # the form variable is an instance of hte locationForm class
    context = {"locations": locations, "form": form}
    return render(request, "Location/index.html", context)

# def add(request):
#     print(request.POST)
    # Location models
    # querysetl
    # select * form Location
    # ORM Object relationship manager
    #.get will return an instance or an error message
    #.filter will return a queryset => empty queryset
    #locations = Location.objects.filter(id=30)
 # SANITIZE  QUERY MANAGER< ORM OBJECT REPRESENTATION < nosql 
 # speed
 # chat : get me all the locations 
 # chat : select * from locations =>
 # not determictict 
 # selct looooool;
 # run it with code:
 # return the result
    # query = "SELECT * from Location where id= " + id
    # query = "SELECT * from Location where id=;drop DATABASE;
    # sql injection
    # connector 
    # connection,cursor(query)
    # close 
    # locations is a queryset set, almost like a list
    # locations[:10]


# class function