from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect

from .models import Squirrel
from django.db.models import Avg

from .forms import AddSightingsForm


def map(request) :
    squirrels = Squirrel.objects.all()[:100]
    context = {
            'squirrels': squirrels
            }
    return render(request, 'map/index.html', context)

def sightings(request):
    squirrels = Squirrel.objects.all()
    context={
        'squirrels': squirrels
        }

    return render (request, 'sightings/main.html', context)

def unique(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, unique_id=squirrel_id)
    if request.method == 'POST':
        form = AddSightingsForm(request.POST, instance=squirrel)
        if  form.is_valid():
            updated_form = form.save()
            return HttpResponseRedirect('/sightings/')
    else:
        form = AddSightingsForm(instance=squirrel)
    
    context  = {
        'squirrel':squirrel,
        'form':form
        }

    return render(request, 'sightings/unique.html',context)

def add(request):
    if request.method == 'POST':
        form =AddSightingsForm(request.POST)
        if  form.is_valid():
            form.save()
            return HttpResponseRedirect('/sightings/')
    else:
        form = AddSightingsForm()
    return render(request, 'sightings/add.html', {'form':form})



def  stats(request):
    total_sightings = Squirrel.objects.count()
    adults = Squirrel.objects.filter(age='Adult').count()
    juveniles = Squirrel.objects.filter(age='Juvenile').count()
    shifts = Squirrel.objects.filter(shift='AM').count()
    latitude = Squirrel.objects.aggregate( _=Avg('latitude'))
    longitude = Squirrel.objects.aggregate( _=Avg('longitude'))

    context={
            'total_sightings': total_sightings,
            'adults' :adults,
            'juveniles':juveniles,
            'shifts': shifts,
            'latitude':latitude,
            'longitude':longitude
        }
    return render(request, 'sightings/stats.html',context)
