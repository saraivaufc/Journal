from django.conf.urls import patterns, include, url
from newspaper.views.userAuthenticated import manager

urlpatterns = patterns('',
	url(r'^$', manager),
	url(r'^section=(?P<id_section>\d+)/$', manager),
	url(r'^section=(?P<id_section>\d+)/subsection=(?P<id_subsection>\d+)/$', manager),
	url(r'^page=(?P<id_page>\d+)/$', manager),
	url(r'^section=(?P<id_section>\d+)/page=(?P<id_page>\d+)/$', manager),
	url(r'^section=(?P<id_section>\d+)/subsection=(?P<id_subsection>\d+)/$', manager),
	url(r'^section=(?P<id_section>\d+)/subsection=(?P<id_subsection>\d+)/page=(?P<id_page>\d+)/$', manager),
)