from django.conf.urls import patterns, include, url
from newspaper.views.userAuthenticated import addNews, remNews, editNews

urlpatterns = patterns('',
	url(r'^add/$', addNews),
	url(r'^edit/(?P<id_news>\d+)/$', editNews),
	url(r'^rem/(?P<id_news>\d+)/$', remNews),
)