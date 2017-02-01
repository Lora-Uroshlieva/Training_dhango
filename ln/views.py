from django.http import HttpResponse, HttpResponseNotFound

from ln import  models


def dashboard(request):
    r = models.Movie.objects.all()

    return HttpResponse(r)
    #return HttpResponseNotFound('Hello')