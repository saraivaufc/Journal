from django.conf.urls import patterns, include, url
from newspaper.views.user import login

urlpatterns = patterns('',
	url(r'^login/$', login),
)