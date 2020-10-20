from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import JsonResponse

from .models import Squirrel

#def index(request):
    #squirrels = Squirrel.object.all()
    #context = {
    #        'squirrels': squirrels,
    #}

    #return render(request, 'map/index.html', context)
   # return HttpResponse("Testing the index(request) in views.py ")

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
    context  = {
        'squirrel':squirrel
    }

    return render(request, 'sightings/unique.html', context)


def add(request):
#    if request.method == 'POST':
#        form =AddSightingsForm(request.POST)
#        if  form.is_valid():
#            form.save()
#            return JsonRespnse({})
#        else:
#           return JsonResponse({'errors': form.errors}, status=400)
    
    return render(request, 'sightings/add.html', {})



def  stats(request):
    return render(request, 'sightings/stats.html',{})
