from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # path('', views.home_page, name='home'),
    path('', views.ArticleListView.as_view(), name='home'),
    path('post/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail')

    # path('post/<slug:slug>/', views.article_detail, name='article_detail')
]
