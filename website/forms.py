from django import forms
import re
from .models import Subscribe

# the mail subscribe form
class NameForm(forms.Form):
    studmail = forms.CharField(max_length=20, label='', required=False, widget=forms.TextInput(
        attrs={'placeholder': 'NTNU-username', 'id': "studentmail",
               'class': "form-control", 'name': "studmail", 'type': "text",
               'maxlength': "{{ form.studmail.maxlength }}", 'size': "35",
              }))

    class Meta:
        model = Subscribe
        fields = {'studmail',}

    def form_contains_letters(self):

        studmail = self.cleaned_data.get('studmail')

        if re.match("^[A-Za-z]*$", studmail):
            return True
        else:
            return False
