from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^', include('newspaper.urls.userAutheticated.manager')),
	url(r'^manager/', include('newspaper.urls.userAutheticated.manager')),
)
