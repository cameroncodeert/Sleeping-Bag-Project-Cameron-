# Participant/forms.py

from django import forms
from .models import Participant
from SleepingBag.models import SleepingBags

class ParticipantForm(forms.ModelForm):
    sleeping_bag_1 = forms.ModelChoiceField(
        queryset=SleepingBags.objects.none(), 
        required=False, 
        widget=forms.Select(attrs={'class': 'select'})
    )
    sleeping_bag_2 = forms.ModelChoiceField(
        queryset=SleepingBags.objects.none(), 
        required=False, 
        widget=forms.Select(attrs={'class': 'select'})
    )
    date_of_birth = forms.DateField(
        widget=forms.TextInput(attrs={'class': 'datepicker'}),
        label="Geboortedatum"
        )


    class Meta:
        model = Participant
        fields = ['first_name', 'last_name', 'date_of_birth', 'registered_location']
        labels = {
            'first_name': 'Voornaam',  
            'last_name': 'Achternaam',  
            'registered_location': 'Geregistreerde Locatie',
        }

    def __init__(self, *args, **kwargs):
        employee_location = kwargs.pop('employee_location', None)
        super().__init__(*args, **kwargs)
        if employee_location:
            available_bags = SleepingBags.objects.filter(
                location=employee_location,
                linked_participant__isnull=True,
                is_in_facility=True
            )
            self.fields['sleeping_bag_1'].queryset = available_bags
            self.fields['sleeping_bag_2'].queryset = available_bags
