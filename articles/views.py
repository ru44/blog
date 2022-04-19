from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required
# Create your views here.


def art_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/art_list.html', {'articles': articles})


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/art_detail.html', {'article': article})


@login_required(login_url="/accounts/login/")
def art_create(request):
    return render(request, 'articles/art_create.html')
