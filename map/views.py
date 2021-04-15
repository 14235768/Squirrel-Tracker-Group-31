from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from sightings.models import Squirrel

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
            }

    return render(request,'map/index.html', context)
