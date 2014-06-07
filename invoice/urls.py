from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.List, name='InvoiceList')
)
