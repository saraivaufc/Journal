from django.conf.urls import patterns, include, url
from newspaper.views.userAuthenticated import addJournalist, remJournalist

urlpatterns = patterns('',
	url(r'^add/$', addJournalist),
	url(r'^rem/(?P<id_journalist>\d+)/$', remJournalist),
)