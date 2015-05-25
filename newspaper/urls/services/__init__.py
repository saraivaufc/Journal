from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^datetime/', include('newspaper.urls.services.dateAndTime')),
	url(r'^sections/', include('newspaper.urls.services.sections')),
	url(r'^subsections/', include('newspaper.urls.services.subsections')),
)
