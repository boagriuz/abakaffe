from django import forms

# the mail subscribe form
class NameForm(forms.Form):
    studmail = forms.CharField(label='Your student mail', max_length=20)
