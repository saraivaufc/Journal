from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^', include('newspaper.urls.user.home')),
	url(r'^news/', include('newspaper.urls.user.news')),
)
