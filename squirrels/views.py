from django.shortcuts import render
from django.http import HttpResponse

from .models import Squirrel

#def index(request):
    #squirrels = Squirrel.object.all()
    #context = {
    #        'squirrels': squirrels,
    #}

    #return render(request, 'map/index.html', context)
    #return HttpResponse("This is where Sightings View will go.")

def map(request) :
    return render(request, 'map/index.html', {})

def sightings(request):
    return render (request, 'sightings/main.html', {})


#Placeholder for sightings/<unique-squirrel-id>
#def index(request):
#    return HttpResponse("This is where Sightings-unique-id View will go.")



#Placeholder for sightings/add
#def index(request):
#    return HttpResponse("This is where Sightings/add View will go.")
