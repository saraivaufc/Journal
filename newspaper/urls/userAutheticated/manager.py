from django.conf.urls import patterns, include, url
from newspaper.views.userAutheticated import manager

urlpatterns = patterns('',
	url(r'^$', manager),
	url(r'^list/$', manager),
)