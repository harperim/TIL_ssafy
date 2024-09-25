from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:  # data의 data 
        model = Reservation
        fields = '__all__'
        # exclude = ('date',)