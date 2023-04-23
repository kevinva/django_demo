from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Article
import time
import datetime

# Create your views here.


def index(request):
    return HttpResponse(f'请求路径:{request.path}, 请求方法:{request.method}')

def create_test(request):

    article = Article(title = f'My first article_{int(time.time())}', body = 'My first article body')
    article.save()
    return HttpResponse(f'Article create successfully: {article}')


def craete_bulk_test(request):
    articles = [
        Article(title = f'My first article_{int(time.time())}', body = 'My first article body'),
        Article(title = f'My second article_{int(time.time()) + 1}', body = 'My second article body'),
        Article(title = f'My third article_{int(time.time()) + 2}', body = 'My third article body'),
    ]
    Article.objects.bulk_create(articles)
    return HttpResponse(f'Articles create successfully: {articles}')

def delete_by_id(request, aid):
    article = Article.objects.get(id = aid)
    article.delete()
    return HttpResponse(f'Article delete successfully: {article}')

### 不设置这个装饰器，POST请求会报403错误
@csrf_exempt
def delete_by_title(request):
    if request.method == 'POST':
        print(f'{request.POST}')

        request_dict = request.POST.dict()
        title = request_dict.get('title')
        print(f'title: {title}')
        article = Article.objects.filter(title__icontains = title)
        article.delete()
        return HttpResponse(f'Article delete successfully: {article}')
    
    return HttpResponse('Article delete failed!')


@csrf_exempt
def update_test(request):
    if request.method == 'POST':
        aid = request.POST.get('id')
        print(f'aid: {aid}')
        article = Article.objects.get(id = aid)
        article.title = 'Hoho Article'
        article.save()
        return HttpResponse(f'Article update successfully: {article}')
    return HttpResponse('Article update failed!')


def query_test(request):
    # articles = Article.objects.all()
    # articles = Article.objects.all().values()
    # articles = Article.objects.all().values('title')
    # articles = Article.objects.all().values_list('title')
    # articles = Article.objects.all().values_list('title', flat = True)
    articles = Article.objects.filter(created__gt = datetime.datetime(2023, 4, 21, 2, 45, 0))

    return HttpResponse(f'articles: {articles}')

    # article = Article.objects.get(id = 1)
    # article = Article.objects.filter(id=1).first()
    # article = get_object_or_404(Article, id = 1)
    # return HttpResponse(f'articles: {article}')

