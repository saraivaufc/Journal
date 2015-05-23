from django.conf.urls import patterns, include, url
from newspaper.views.userAuthenticated import addClassifield, remClassifield, editClassifield, viewClassifield 

urlpatterns = patterns('',
	url(r'^add/$', addClassifield),
	url(r'^view/$', viewClassifield),
	url(r'^view/page=(?P<id_page>\d+)/$', viewClassifield),
	url(r'^edit/(?P<id_classifield>\d+)/$', editClassifield),
	url(r'^rem/(?P<id_classifield>\d+)/$', remClassifield),
)