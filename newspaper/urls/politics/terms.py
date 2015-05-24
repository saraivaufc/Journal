from django.conf.urls import patterns, include, url
from newspaper.views.politics import viewTerms
urlpatterns = patterns('',
	url(r'^viewterms/$', viewTerms),
)

