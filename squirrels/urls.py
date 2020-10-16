from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('sightings', views.trial, name='trial') # not sure if we need an extra one here
]
