from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^datetime/', include('newspaper.urls.services.dateAndTime')),
)
