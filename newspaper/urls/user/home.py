from django.conf.urls import patterns, include, url
from newspaper.views.user import *

urlpatterns = patterns('',
	url(r'^$', home),
	url(r'^page=(?P<id_page>\d+)/$', home),
	url(r'^section=(?P<id_section>\d+)/$', home),
	url(r'^section=(?P<id_section>\d+)/page=(?P<id_page>\d+)/$', home),
	url(r'^section=(?P<id_section>\d+)/subsection=(?P<id_subsection>\d+)/$', home),
	url(r'^section=(?P<id_section>\d+)/subsection=(?P<id_subsection>\d+)/page=(?P<id_page>\d+)/$', home),
)