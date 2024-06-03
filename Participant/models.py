from django.db import models
from django.core.exceptions import ValidationError
from Location.models import Location

# Create your models here.
class Participant(models.Model):
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
        ('other','other')
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    registered_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    document_type = models.CharField(max_length=30, choices=DOCUMENT_TYPES) 
    document_date = models.DateField(null=True, blank=True) 
    custom_document_type = models.CharField(max_length=100, blank=True, null=True)  

    class Meta:
        unique_together = ['first_name', 'last_name', 'date_of_birth']
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def save(self, *args, **kwargs):
        # are we creating a new participant or are we updating participant
        # if self.pk and not self.is_active:
        #     bags = SleepingBags.objects.filter(linked_participant=self, is_in_facility=False)
        #     bags.status = 'Lost'
        #     bags.save()
        #     bags.status = 'lost'


        if self.document_type=='other' and self.custom_document_type == None:
            raise ValidationError('A custom document need to be added since it is a document of type other')
        super(Participant, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name
    