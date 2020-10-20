from django.urls import path

from . import views

app_name = 'squirrels'

urlpatterns = [
   # path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('sightings/', views.sightings, name='sightings'),
    path('sightings/add/', views.add, name='add'),
    path('sightings/stats/', views.stats, name='stats'),
    path('sightings/<squirrel_id>/', views.unique, name='unique')
]


