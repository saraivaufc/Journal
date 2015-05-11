from django.conf.urls import patterns, include, url
from newspaper.views.user import viewNews
from newspaper.views.user import home

urlpatterns = patterns('',
	url(r'^$', home),
	url(r'^(?P<id_news>\d+)/$', viewNews),
)