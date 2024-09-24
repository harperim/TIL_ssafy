from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):
    # 전체 게시물을 가져오기 (QuerySet)
    articles = Article.objects.all()
    # context로 포장하기
    context = {
        'articles': articles,
    }
    # 템플릿으로 context 보내기
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    # 1. pk 값에 해당하는 단일 게시물 가져오기(instance)
    article = Article.objects.get(pk=pk)
    # 2. context로 포장하기
    context = {
        'article': article
    }
    # 3. 템플릿으로 context 보내기 
    return render(request, 'articles/detail.html', context)


def create(request):
    # 1. POST 딕셔너리에서 title 과 content 받아오기
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # 2. Article() 생성자로 초기화
    article = Article(title=title, content=content)

    # 3. 저장
    article.save()
    return redirect('articles:detail', article.pk)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    # 1. 게시물 하나 가져오기
    article = Article.objects.get(pk=pk)
    # 2. 사용자가 수정한 글 제목, 글 내용 저장하기
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    # 3. DB에 저장하기 
    article.save()
    return redirect('articles:detail', article.pk)
