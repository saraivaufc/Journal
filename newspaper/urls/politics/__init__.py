from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^terms/', include('newspaper.urls.politics.terms')),
)

