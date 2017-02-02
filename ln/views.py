from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from ln import models


def dashboard(request):
    movies = models.Movie.objects.all()

    return render(request, 'dashboard.html', {'movies': movies})

@login_required
def movie_order(request, movie_id):
    print(movie_id)
    messages.info(request, 'Go to %s' % movie_id)
    return redirect('dashboard')

