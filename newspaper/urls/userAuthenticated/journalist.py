from django.conf.urls import patterns, include, url
from newspaper.views.userAuthenticated import addJournalist, remJournalist, editJournalist, viewJournalist 

urlpatterns = patterns('',
	url(r'^add/$', addJournalist),
	url(r'^view/(?P<id_journalist>\d+)/$', viewJournalist),
	url(r'^edit/(?P<id_journalist>\d+)/$', editJournalist),
	url(r'^rem/(?P<id_journalist>\d+)/$', remJournalist),
)