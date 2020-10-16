from django.shortcuts import render
#from django.http import HttpResponse


def index(request):
    #return HttpResponse('Ths is where Maps will go')
    return render(request, 'map/index.html', {})


#Placeholder for sightings
#def trials(request):
#    return HttpResponse("This is where Sightings View will go.")


#Placeholder for sightings/<unique-squirrel-id>
#def index(request):
#    return HttpResponse("This is where Sightings-unique-id View will go.")



#Placeholder for sightings/add
#def index(request):
#    return HttpResponse("This is where Sightings/add View will go.")
