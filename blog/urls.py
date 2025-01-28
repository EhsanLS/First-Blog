from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('post/<slug:slug>/', views.article_detail, name='article_detail')
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
