from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect

from .models import Squirrel

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

#def unique(request, squirrel_id):
#    squirrel = get_object_or_404(Squirrel, unique_id=squirrel_id)
#    context  = {
#        'squirrel':squirrel
#    }

#    return render(request, 'sightings/unique.html', context)

def unique(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, unique_id=squirrel_id)
    form = AddSightingsForm()
    context  = {
        'squirrel':squirrel,
        'form':form
        }

    if request.method == 'POST':
        form =AddSightingsForm(request.POST)
        if  form.is_valid():
            form.save()
            return HttpResponseRedirect('/sightings/<unique_id>')
    else:
        form = AddSightingsForm()    
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
    context={
            'total_sightings': total_sightings,
            'adults' :adults,
            'juveniles':juveniles

        }
    
    return render(request, 'sightings/stats.html',context)
