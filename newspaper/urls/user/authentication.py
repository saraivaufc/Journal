from django.conf.urls import patterns, include, url
from newspaper.views.user import login, signup, logout

urlpatterns = patterns('',
	url(r'^login/$', login),
	url(r'^logout/$', logout),
	url(r'^signup/$', signup),
)