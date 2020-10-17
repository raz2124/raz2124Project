from django.urls import path

from . import views

app_name = 'squirrels'

urlpatterns = [
   # path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('sightings/', views.sightings, name='sightings')
    #path('sightings/<unique_id>/', views.unique, name='unique=squirrel_id')
]


