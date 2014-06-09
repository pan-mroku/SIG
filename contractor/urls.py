from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.List, name='ContractorList'),
    url(r'^edit/', views.Edit, name='ContractorEdit'),
    url(r'^add/', views.Add, name='ContractorAdd'),
    url(r'^delete/', views.Delete, name='ContractorDel'),
)
