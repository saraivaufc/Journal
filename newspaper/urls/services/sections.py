from django.conf.urls import patterns, include, url
from newspaper.views.services import sections

urlpatterns = patterns('',
	url(r'^all/$', sections),
)