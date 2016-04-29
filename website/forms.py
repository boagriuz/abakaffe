from django import forms

# the mail subscribe form
class NameForm(forms.Form):
    studmail = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Your student mail'}))
