import uuid

from django.shortcuts import render, redirect

from ln.user.forms import RegistrationForm, LoginForm
from ln.models import User, Session


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            if not User.objects.registration(
                form.cleaned_data['login'],
                form.cleaned_data['password']
            ):
                pass
            return redirect('user:success_registration')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', context={'form': form})


def success_registration(request):
    return render(request, 'success_registration.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            session = Session.objects.create(
                user=form.user, token=uuid.uuid4())

            response = redirect('dashboard')
            response.set_cookie('user-session', session.token, expires=session.date_expired)

            return response
    else:
        form = LoginForm()

    return render(request, 'login.html', context={'form': form})

