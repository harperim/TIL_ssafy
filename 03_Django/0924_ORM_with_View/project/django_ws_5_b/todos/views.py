from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    # work = request.GET.get('work')
    todo_list = Todo.objects.all()
    context = {
        # 'work': work
        'todo_list': todo_list
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    work = request.POST.get('work')
    content = request.POST.get('content')
    work = Todo(work=work, content=content)
    work.save()
    # return render(request, 'todos/create_todo.html')
    return redirect('todos:detail', work.pk)


def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)


# # (1) 수정
# def new_todo(request, pk):
#     work = Todo.objects.get(pk=pk)
#     context = {
#         'work': work,
#     }
#     return render(request, 'todos/new_todo.html', context)

# # (2) 수정 후 업데이트
# def update(request, pk):
#     work = Todo.objects.get(pk=pk)
#     work.work = request.POST.get('work')
#     work.content = request.POST.get('content')
#     work.save()
#     return redirect('todos:detail', work.pk)


# 삭제
def delete(request, pk):
    work = Todo.objects.get(pk=pk)
    work.delete()
    return redirect('todos:index')