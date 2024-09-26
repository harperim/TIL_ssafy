from django.shortcuts import render, redirect
# 모델 클래스 가져오기
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    # url로부터 전달받은 pk를 활용해 데이터를 조회
    # article = Article.objects.get(id=pk)
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    # 어떤 게시글 삭제할지 조회
    article = Article.objects.get(pk=pk)

    # 조회한 게시글 삭제
    article.delete()
    return redirect('articles:index')


def create(request):
    # method를 구분하여 글쓰기폼과 글 저장을 처리 
    if request.method == "POST":
        form = ArticleForm(data=request.POST)
        # 유효성 검사
        if form.is_valid():  # 통과했을 때
            article = form.save()
            return redirect('articles:detail', article.pk)

    else:  # POST가 아닌 경우 (a href)
        form = ArticleForm()

    # 통과 안 했을 때
    # 입력폼으로 다시 되돌아가게(form 정보-유효성 통과 못함) 제목 미작성, 내용 미작성
    # 유효성 검사의 else 부분과 else 부분 둘 다에 해당되므로 이 위치에 입력
    # 1. 유효성 검사 통과 못한 경우, 2. POST 방식이 아닌 경우 
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
