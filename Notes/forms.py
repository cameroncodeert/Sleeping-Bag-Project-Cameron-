from django import forms
from django.forms import ModelForm
from .models import Note

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["note", "participant"]
        # widgets = {
        #     'participant': forms.HiddenInput(),
        # }
    def __init__(self, hidden=False, *args, **kwargs, ):
        super(NoteForm, self).__init__(*args, **kwargs)
        if hidden:
            self.fields['participant'].widget = forms.HiddenInput()  # Hide participant field

# form = NoteForm() note particpant writable
# other_form = NoteForm(disabled=True, initial_va)
