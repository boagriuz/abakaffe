from django import forms
from django.contrib.auth.models import User
import re


# the mail subscribe form
class NameForm(forms.Form):
    studmail = forms.CharField(max_length=20, label='', required=False, widget=forms.TextInput(
        attrs={'placeholder': 'NTNU-username', 'id': "{{ form.studmail.id_for_label }}",
               'class': "form-control", 'name': "studmail", 'type': "text",
               'maxlength': "{{ form.studmail.maxlength }}", 'size': "35",
               'autocomplete': "on"}))

    class Meta:
        model = User
        fields = ('studmail',)


    def form_contains_letters(self):

        studmail = self.cleaned_data.get('studmail')

        if studmail == "":
            return False

        if re.match("^[A-Za-z]*$", studmail):
            return True
        else:
            return False
