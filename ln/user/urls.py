from django.conf.urls import url

from ln.user import views

urlpatterns = [
    url(r'^user', views.registration, name='user'),
    url(r'^login', views.login, name='login'),
]
