from django.conf.urls import patterns, include, url
from newspaper.views.user import *

urlpatterns = patterns('',
	url(r'^$', home),
	url(r'^(?P<id_page>\d+)/$', home),
	url(r'^(?P<id_section>\d+)/(?P<id_page>\d+)/$', home),
	url(r'^(?P<id_section>\d+)/(?P<id_subsection>\d+)/(?P<id_page>\d+)/$', home),
)