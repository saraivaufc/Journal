from django.conf.urls import patterns, include, url
from newspaper.views.userAuthenticated import addSection, editSection, remSection

urlpatterns = patterns('',
	url(r'^add/$', addSection),
	url(r'^edit/(?P<id_section>\d+)/$', editSection),
	url(r'^rem/(?P<id_section>\d+)/$', remSection),
)