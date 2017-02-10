from django import forms

from ln.models import User


class RegistrationForm(forms.Form):
    login = forms.CharField(max_length=50, initial='')
    password = forms.CharField(min_length=6, initial='')

    def clean_login(self):
        login = self.cleaned_data['login']
        if User.objects.filter(login=login).first():
            raise forms.ValidationError('User with login "%s" exists' % login)

        return login
