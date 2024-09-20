from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'accounts/login.html')


def detail(request):
    id = request.GET.get('id')
    password = request.GET.get('passwords')
    user = {
        'id': id,
        'password': password,
    }
    return render(request, 'accounts/datial.html', user)



