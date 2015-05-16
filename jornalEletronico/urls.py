from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from newspaper.views import index
from newspaper.feeds import NewsLatests

admin.autodiscover()

urlpatterns = patterns('',
	url(r'$^', index ),
	url(r'^newspaper/', include('newspaper.urls', namespace="newspaper", app_name="newspaper")),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
	url(r'^admin/', include(admin.site.urls)),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^feed/$', NewsLatests()),
)
