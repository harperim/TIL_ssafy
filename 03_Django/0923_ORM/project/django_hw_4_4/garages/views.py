from django.shortcuts import render
from .models import Garage


# Create your views here.
def index(request):
    garages = Garage.objects.all()
    dokdo_garages = Garage.objects.filter(location='독도')
    thirty_unders = Garage.objects.filter(capacity__lte=30)
    available_garages = Garage.objects.filter(is_parking_avaliable=True)

    context = {
        'garages': garages,
        'dokdo_garages': dokdo_garages,
        'thirty_unders': thirty_unders,
        'available_garages': available_garages,
    }
    return render(request, 'garages/index.html', context)
