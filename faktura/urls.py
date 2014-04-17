from django.conf.urls import patterns, url

from faktura import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
