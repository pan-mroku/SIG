# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
import views

urlpatterns = patterns('',
    url(r'^$', views.zarejestruj, name='zarejestruj'),
    url(r'zaloguj/$', views.zaloguj, name="zaloguj"),
    url(r'logowanie/$', views.logowanie, name="logowanie"),
    url(r'rejestracja/$', views.rejestracja, name="rejestracja"),
    url(r'zarejestruj/$', views.zarejestruj, name="zarejestruj"),
    url(r'wyloguj/$', views.wyloguj, name="wyloguj"),
    #po co to? to developmentu wystaczy STATICFILES_DIRS, a na serwerzer zrobi się collectstatic
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'})
)
