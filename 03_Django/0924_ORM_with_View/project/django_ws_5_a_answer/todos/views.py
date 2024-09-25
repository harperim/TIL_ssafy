from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    # work = request.GET.get('work')
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')


def create_todo_ok(request):
    work = request.POST.get('work')
    content = request.POST.get('content')
    is_completed = False
    todo = Todo(work=work, content=content, is_completed=is_completed)
    todo.save()
    return redirect('todos:detail', todo.pk)


def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo,
    }
    return render(request, 'todos/detail.html', context)


# def detail(request, pk):
#     work = Todo.objects.get(pk=pk)
#     context = {
#         'work': work,
#     }
#     return render(request, 'todos/detail.html', context)
    


# def detail(request, pk):
#     # 1. pk 값에 해당하는 단일 게시물 가져오기(instance)
#     article = Article.objects.get(pk=pk)
#     # 2. context로 포장하기
#     context = {
#         'article': article
#     }
#     # 3. 템플릿으로 context 보내기 
#     return render(request, 'articles/detail.html', context)