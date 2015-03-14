from django.conf.urls import patterns, include, url
from newspaper.views.user import viewNews

urlpatterns = patterns('',
	url(r'^(?P<id_news>\d+)/$', viewNews),
)