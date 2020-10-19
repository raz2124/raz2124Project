from django.shortcuts import render
from django.shortcuts import get_object_or_404
#from django.http import HttpResponse

from .models import Squirrel

#def index(request):
    #squirrels = Squirrel.object.all()
    #context = {
    #        'squirrels': squirrels,
    #}

    #return render(request, 'map/index.html', context)
   # return HttpResponse("Testing the index(request) in views.py ")

def map(request) :
    return render(request, 'map/index.html', {})

def sightings(request):
    squirrels = Squirrel.objects.all()
    #squirrels.date = object.date()
    context={
        'squirrels': squirrels,
        #'squirrels.date': squirrels.date, 
        }

    return render (request, 'sightings/main.html', context)

def unique(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, unique_id=squirrel_id)
    context  = {
        'squirrel':squirrel
    }

    return render(request, 'sightings/unique.html', context)

#Placeholder for sightings/add
#def index(request):
#    return HttpResponse("This is where Sightings/add View will go.")
