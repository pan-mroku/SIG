from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^invoice/', include('invoice.urls')),
    url(r'^article/', include('article.urls')),
	url(r'^register/', include('register.urls')),
)
