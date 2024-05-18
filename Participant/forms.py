# Participant/forms.py

from django import forms
from .models import Participant
from SleepingBag.models import SleepingBags

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
            available_bags = SleepingBags.objects.filter(
                location=employee_location,
                linked_participant__isnull=True,
                is_in_facility=True
            )
            self.fields['sleeping_bag_1'].queryset = available_bags
            self.fields['sleeping_bag_2'].queryset = available_bags
