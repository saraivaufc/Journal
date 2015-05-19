from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^', include('newspaper.urls.user.home')),
	url(r'^news/', include('newspaper.urls.user.news')),
	url(r'^classifield/', include('newspaper.urls.user.classifield')),
	url(r'^authentication/', include('newspaper.urls.user.authentication')),
	url(r'^search/', include('newspaper.urls.user.search')),
)
