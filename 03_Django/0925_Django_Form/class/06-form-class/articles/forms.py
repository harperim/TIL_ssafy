from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:  # data의 data 
        model = Article
        fields = '__all__'
        exclude = ('title',)

