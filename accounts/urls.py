# from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name="signup")
]
