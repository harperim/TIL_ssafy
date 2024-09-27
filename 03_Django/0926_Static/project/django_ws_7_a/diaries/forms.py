from django import forms
from .models import Diary

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = '__all__'
        # fields = ('content', 'created_at', )  # 포함할 필드
        # exclude = ('created_at', )  # 제외할 필드 