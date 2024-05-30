from django import forms
from django.forms import ModelForm
from .models import Note
from Participant.models import Participant
class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["note", "participant"]
        # widgets = {
        #     'participant': forms.HiddenInput(),
        # }
    # def __init__(self, hidden=False, *args, **kwargs, ):
    #     super(NoteForm, self).__init__(*args, **kwargs)
    #     if hidden:
    #         HiddenParticipantParticipantHiddenself.fields['participant'].widget = forms.HiddenInput()  # Hide participant field
class NoteFormHiddenParticipant(ModelForm):
    class Meta:
        model = Note
        fields = ["note", "participant"]        
        widgets = {
            'participant': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        participant = kwargs.pop('participant', None)
        super(NoteFormHiddenParticipant, self).__init__(*args, **kwargs)
        if participant:
            self.fields['participant'].initial = participant
        self.fields['participant'].queryset = Participant.objects.filter(id=participant.id) if participant else Participant.objects.none()


   #  def __init__(self,*args, **kwargs):
    #     # Access the location from initial, if it's provided
    #     initial_location = kwargs.get('initial', {}).get('location', None)
    #     super().__init__(*args, **kwargs)

    #     # Filter the queryset based on initial_location
    #     if initial_location:
    #         self.fields['participant'].queryset = Participant.objects.filter(
    #             registered_location=initial_location
    # #         )
# 
# class NoteFormParticipantHidden(ModelForm):
#     class Meta:
#         model = Note
#         fields = [" w 'participant': forms.HiddenInput(),}
            # idgets = {
#          
#     def __init(self, location=None, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if location:
#              self.fields['participant'].queryset = Participant.objects.filter(
#                 registered_location=location
#             )  # Filter t   'participant': forms.HiddenInput(),
#     #     }
# selflocation, =, location=No)#     # def __init__(skwf, *args, **kwargs):
#         location= kwargs.pop('location', None) 
#         super().__init__(*args, **kwargs)

# #     #     if location:
#     #         # employee = Employee.objects.get(user=user)  
#     #         self.fields['participant'].queryset = Participant.objects.filter(
#     #             registered_location=location
          #   )  # Filter the queryset


# form = NoteForm() note particpant writable
# other_form = NoteForm(disabled=True, initial_va)
