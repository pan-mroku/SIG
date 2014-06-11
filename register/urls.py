# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
import views

urlpatterns = patterns('',
    url(r'^$', views.registerform, name='registerform'),
    url(r'loginform/$', views.loginform, name="loginform"),
    url(r'loginprocess/$', views.loginprocess, name="loginprocess"),
    url(r'registerform/$', views.registerform, name="registerform"),
    url(r'registerprocess/$', views.registerprocess, name="registerprocess"),
    url(r'logoutprocess/$', views.logoutprocess, name="logoutprocess"),
)
