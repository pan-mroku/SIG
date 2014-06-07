from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.List, name='ArticleList'),
    url(r'^edit/', views.Edit, name='ArticleEdit'),
    url(r'^add/', views.Add, name='ArticleAdd'),
    url(r'^delete/', views.Delete, name='ArticleDel'),
)
