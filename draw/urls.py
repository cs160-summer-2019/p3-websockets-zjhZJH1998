# chat/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'), 
  
    url(r'^create$', views.create, name='create'),
    url(r'^composeMusic$', views.composeMusic, name='composeMusic'),
  url(r'^play$', views.play, name='play'),
]

