from django.shortcuts import render

# Create your views here.
def index(request):
    work = request.GET.get('work')
    context = {
        'work': work
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    work = request.GET.get('work')
    context = {
        'work': work
    }
    return render(request, 'todos/create_todo.html', context)

def detail(request, work):
    context = {
        'work': work
    }
    return render(request, 'todos/detail.html', context)