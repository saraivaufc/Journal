from django.conf.urls import patterns, include, url
from newspaper.views.userAuthenticated import addRedator, remRedator, editRedator, viewRedator 

urlpatterns = patterns('',
	url(r'^add/$', addRedator),
	url(r'^view/(?P<id_redator>\d+)/$', viewRedator),
	url(r'^edit/(?P<id_redator>\d+)/$', editRedator),
	url(r'^rem/(?P<id_redator>\d+)/$', remRedator),
)