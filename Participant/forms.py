# Participant/forms.py

from django import forms
from .models import Participant
from SleepingBag.models import SleepingBags
from django.forms.widgets import TextInput

class ParticipantForm2(forms.ModelForm):
    
    sleeping_bag_1 = forms.ModelChoiceField(
        queryset=SleepingBags.objects.none(), 
        widget=forms.Select(attrs={'class': 'select'})
    )
    sleeping_bag_2 = forms.ModelChoiceField(
        queryset=SleepingBags.objects.none(), 
        widget=forms.Select(attrs={'class': 'select'})
    )
    
    class Meta:
        model = Participant
        fields = ["first_name", "last_name", "registered_location", "date_of_birth", "document_type", "document_date", "custom_document_type"]
    
    def clean(self):
        cleaned_data = super().clean()
        print('cleaned data', cleaned_data)
        document_type = cleaned_data.get("document_type")
        custom_document_type = cleaned_data.get("custom_document_type")
        print("custom document type", custom_document_type)

        if document_type == 'other' and not custom_document_type:
            self.add_error('custom_document_type', 'A custom document type needs to be added since the document is of type "other".')

        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        employee_location = kwargs.pop('employee_location', None)
        super().__init__(*args, **kwargs)
        if employee_location:
            self.fields['registered_location'].widget = forms.HiddenInput() 
            self.fields["date_of_birth"].widget = TextInput(attrs={'class': 'datepicker'})
            self.fields["document_date"].widget = TextInput(attrs={'class': 'datepicker'})
            self.fields['registered_location'].initial = employee_location 
            available_bags = SleepingBags.objects.filter(
                location=employee_location,
                linked_participant__isnull=True,
                is_in_facility=True
            )
            self.fields['sleeping_bag_1'].queryset = available_bags
            self.fields['sleeping_bag_2'].queryset = available_bags


class ParticipantForm(forms.ModelForm):
    DOCUMENT_TYPES = [
        ('employment_contract', 'Arbeidsovereenkomst'),
        ('bank_statement', 'Bankafschrift'),
        ('birth_certificate', 'Geboorteakte'),
        ('proof_of_address', 'Bewijs van Adres'),
        ('tax_documents', 'Belastingdocumenten'),
        ('educational_certificates', 'Onderwijscertificaten'),
        ('immigration_documents', 'Immigratiedocumenten'),
        ('health_insurance_card', 'Zorgverzekeringskaart'),
        ('rental_agreement', 'Huurcontract'),
        ('marriage_certificate', 'Huwelijksakte'),
        ('id_card', 'Identiteitskaart'),
        ('insurance_policies', 'Verzekeringspolissen'),
        ('medical_records', 'Medische dossiers'),
        ('utility_bill', 'Nutskostenrekening'),
        ('passport', 'Paspoort'),
        ('residence_permit', 'Verblijfsvergunning'),
        ('drivers_license', 'Rijbewijs'),
        ('social_security_card', 'Socialezekerheidskaart'),
        ('vehicle_registration', 'Kentekenbewijs'),
        ('work_permit', 'Werkvergunning'),
        ('Other', 'Other'),

    ]
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
    document_type = forms.ChoiceField(choices=DOCUMENT_TYPES, label="Type Document") 
    custom_document_type = forms.CharField(required=False, label="Ander Document Type", widget=forms.TextInput(attrs={'class': 'input'}))  
    document_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}), label="Datum van het Document")  


    class Meta:
        model = Participant
        fields = ['first_name', 'last_name', 'date_of_birth', 'registered_location']
        labels = {
            'first_name': 'Voornaam',  
            'last_name': 'Achternaam',  
            'registered_location': 'Geregistreerde Locatie',
            'document_type': 'Type Document',
            'custom_document_type': 'Ander Document Type',
            'document_date': 'Datum van het Document'
        }

    def __init__(self, *args, **kwargs):
        employee_location = kwargs.pop('employee_location', None)
        super().__init__(*args, **kwargs)
        if employee_location:
            self.fields['registered_location'].widget = TextInput(attrs={'readonly': True}) 
            self.fields['registered_location'].initial = employee_location.name  
            available_bags = SleepingBags.objects.filter(
                location=employee_location,
                linked_participant__isnull=True,
                is_in_facility=True
            )
            self.fields['sleeping_bag_1'].queryset = available_bags
            self.fields['sleeping_bag_2'].queryset = available_bags
