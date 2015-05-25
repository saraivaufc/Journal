from django.conf.urls import patterns, include, url
from newspaper.views.user import search

urlpatterns = patterns('',
	url(r'^news/$', search),
)