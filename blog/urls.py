from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from articles import views as art_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('', art_views.art_list, name="home"),
    path('accounts/', include('accounts.urls')),
    path('art/', include('articles.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
