from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Article
from .forms import ArticleForm


def index(request):
    latest_articles = Article.objects.order_by('-pub_date')
    print(latest_articles)
    return render(request, 'blog/article_list.html', {'latest_articles': latest_articles})


def article_detail(request, aid):
    article = get_object_or_404(Article, id = aid)
    return render(request, 'blog/article_detail.html', {'article': article})

@csrf_exempt
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:article_list'))
    else:
        form = ArticleForm()
    return render(request, 'blog/article_form.html', {'form': form})

@csrf_exempt
def article_update(request, aid):
    article_obj = get_object_or_404(Article, id = aid)
    if request.method == 'POST':
        form = ArticleForm(instance = article_obj, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:article_detail', args = [aid,]))
    else:
        form = ArticleForm(instance = article_obj)
    return render(request, 'blog/article_form.html', {'form': form, 'object': article_obj})