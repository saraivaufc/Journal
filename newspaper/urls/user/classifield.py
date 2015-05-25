from django.conf.urls import patterns, include, url
from newspaper.views.user import viewClassifield

urlpatterns = patterns('',
	url(r'^(?P<id_classifield>\d+)/$', viewClassifield),
)