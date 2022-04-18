from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from requests import request

import articles
from .models import Article
# Create your views here.


def art_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/art_list.html', {'articles': articles})


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/art_detail.html', {'article': article})
