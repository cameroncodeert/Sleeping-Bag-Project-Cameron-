import datetime
from django.shortcuts import render
from .models import Location
from django.forms import ModelForm

# Form for Location data management
class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'address', 'max_capacity']

# View to handle Location management
def manageLocation(request):
    if request.method== "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            max_capacity = form.cleaned_data['max_capacity']
            location = Location(name=name, address=address, max_capacity=max_capacity)
            location.save()
            # Save new location to the database




    locations = Location.objects.all()
    form = LocationForm()
    # the form variable is an instance of hte locationForm class
    context = {"locations": locations, "form": form}
    return render(request, "Location/index.html", context)
    # Display all locations and the form for creating a new one


