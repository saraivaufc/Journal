from django.conf.urls import patterns, include, url
from newspaper.views.userAuthenticated import addNews, remNews

urlpatterns = patterns('',
	url(r'^add/$', addNews),
	url(r'^rem/(?P<id_news>\d+)/$', remNews),
)