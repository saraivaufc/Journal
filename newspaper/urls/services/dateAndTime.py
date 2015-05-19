from django.conf.urls import patterns, include, url
from newspaper.views.services import dateTimeNow

urlpatterns = patterns('',
	url(r'^$', dateTimeNow),
)