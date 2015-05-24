from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^', include('newspaper.urls.userAuthenticated.manager')),
	url(r'^manager/', include('newspaper.urls.userAuthenticated.manager')),
	url(r'^manager/news/', include('newspaper.urls.userAuthenticated.news')),
	url(r'^manager/journalist/', include('newspaper.urls.userAuthenticated.journalist')),
	url(r'^manager/redator/', include('newspaper.urls.userAuthenticated.redator')),
	url(r'^manager/section/', include('newspaper.urls.userAuthenticated.section')),
	url(r'^manager/subsection/', include('newspaper.urls.userAuthenticated.subsection')),
	url(r'^manager/classifield/', include('newspaper.urls.userAuthenticated.classifield')),
)

