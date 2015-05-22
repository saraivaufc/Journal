from django.conf.urls import patterns, include, url
from newspaper.views.services import subsections

urlpatterns = patterns('',
	url(r'^all/$', subsections),
)