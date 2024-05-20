from django.forms import ModelForm
from django import forms
from .models import SleepingBags

class SleepingBagsForm(ModelForm):
    class Meta:
        model = SleepingBags
        # todo last_washing_cycle should be read_only fiedl
        fields = ["status", "is_washed", "is_in_facility" ]
        widgets = {
            'linked_participant': forms.HiddenInput(),
            # "last_washing_cycle": forms.
        }
    # def __init__(self, *args, **kwargs):
    #     super(SleepingBags, self).__init__(*args, **kwargs)
    #     if self.instance and self.instance.pk:
    #         self.fields['pk'].initial = self.instance.id


    # def __init__(self, *args, **kwargs):
    #     super(SleepingBagsForm, self).__init__(*args, **kwargs)
    #     self.fields['last_washing_cycle'].disabled = True
    #     self.fields['last_washing_cycle'].widget.attrs['readonly'] = True



    #not used but get error when removed:


from .models import StatusChoice
class SleepingBagsCustomForm(forms.Form):
    bag_number = forms.CharField(label="The bag number", max_length=34)
    status = forms.CharField(widget=forms.Select(choices= StatusChoice.choices ))
    is_washed = forms.BooleanField()
    is_in_facility = forms.BooleanField()
