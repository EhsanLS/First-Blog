from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('post/<slug:slug>/', views.article_detail, name='article_detail')
]
