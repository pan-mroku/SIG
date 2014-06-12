from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.List, name='InvoiceList'),
    url(r'^edit/', views.Edit, name='InvoiceEdit'),
    url(r'^add/', views.Add, name='InvoiceAdd'),
    url(r'^delete/', views.Delete, name='InvoiceDel'),
    url(r'^view/', views.View, name='InvoiceView'),
    url(r'^paid/', views.SetDateOfPayment, name='InvoiceSetDate'),
)
