from django.shortcuts import render

from ln.user.forms import RegistrationForm


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            print(request.POST)
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', context={'form': form})


def login(request):
    return render(request, 'login.html')
