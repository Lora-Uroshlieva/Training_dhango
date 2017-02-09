from django import forms


class RegistrationForm(forms.Form):
    login = forms.CharField(max_length=50, initial='')
    password = forms.CharField(min_length=6, initial='')
