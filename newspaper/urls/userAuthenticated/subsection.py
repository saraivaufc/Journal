from django.conf.urls import patterns, include, url
from newspaper.views.userAuthenticated import addSubSection, editSubSection, remSubSection

urlpatterns = patterns('',
	url(r'^add/$', addSubSection),
	url(r'^edit/(?P<id_subsection>\d+)/$', editSubSection),
	url(r'^rem/(?P<id_subsection>\d+)/$', remSubSection),
)