from django.shortcuts import render, redirect

from ln.user.forms import RegistrationForm
from ln.models import User


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
    return render(request, 'login.html')
