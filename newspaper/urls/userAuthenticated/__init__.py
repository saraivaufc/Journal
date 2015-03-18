from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^', include('newspaper.urls.userAuthenticated.manager')),
	url(r'^manager/', include('newspaper.urls.userAuthenticated.manager')),
	url(r'^manager/news/', include('newspaper.urls.userAuthenticated.news')),
	url(r'^manager/journalist/', include('newspaper.urls.userAuthenticated.journalist')),
)

