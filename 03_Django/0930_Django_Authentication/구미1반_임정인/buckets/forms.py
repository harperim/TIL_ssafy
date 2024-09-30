from django import forms
from .models import TravelBucketList


class TravelBucketListForm(forms.ModelForm):
    class Meta:
        model = TravelBucketList
        # 07. fields = '__all__' 줄은 주석처리하고 exclude 를 써서 제외할 필드만 지정해준다. 
        # fields = '__all__'
        exclude = ('reason', 'city', )
        widgets = {
            'destination_name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control'}),
            'planned_visit_date': forms.DateInput(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }

