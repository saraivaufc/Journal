from django.conf.urls import patterns, include, url
from newspaper.views import *

urlpatterns = patterns('',
	url(r'^', include('newspaper.urls.user')),
	url(r'^home/', include('newspaper.urls.user')),
	url(r'^userAuthenticated/', include('newspaper.urls.userAutheticated')),
)