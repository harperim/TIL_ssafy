from django.shortcuts import render

# Create your views here.

def introduce_view(request, name):
    context = {
        'name': name
    }
    return render(request, 'my_app/introduce.html', context)

