from django.conf.urls import url

from ln.user import views

urlpatterns = [
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^success_registration/$', views.success_registration, name='success_registration'),
    url(r'^login/$', views.login, name='login'),
]
