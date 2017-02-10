from django import forms
from django.contrib.auth.hashers import check_password

from ln.models import User


class RegistrationForm(forms.Form):
    login = forms.CharField(max_length=50, initial='')
    password = forms.CharField(min_length=6, initial='')

    def clean_login(self):
        login = self.cleaned_data['login']
        if User.objects.filter(login=login).first():
            raise forms.ValidationError('User with login "%s" exists' % login)

        return login


class LoginForm(forms.Form):
    login = forms.CharField(max_length=50, initial='')
    password = forms.CharField(min_length=6, initial='')

    def clean(self):
        cleaned_data = super().clean()

        login = cleaned_data.get('login')
        password = cleaned_data.get('password')
        if not (login and password):
            return

        self.user = User.objects.filter(login=login).first()

        if not (self.user and check_password(password, self.user.password)):
            raise forms.ValidationError('Login or password error')
