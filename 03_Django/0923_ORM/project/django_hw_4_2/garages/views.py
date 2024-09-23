from django.shortcuts import render
from .models import Garage

# Create your views here.
def index(request):
    garages = Garage.objects.all()

    context = {
        'garages': garages,
    }
    return render(request, 'garages/index.html', context)
