from django.urls import path
from . import views

app_name ='article'

urlpatterns = [
    path('', views.art_list, name="list"),
    path('<slug>/', views.article_detail, name="details"),
]
