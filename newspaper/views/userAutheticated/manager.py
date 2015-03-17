# -*- endcoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from newspaper.models import News, Section, SubSection
def manager(request):
	if not request.user.has_perm('newspaper.access_manager'):
		return HttpResponseRedirect("/newspaper/")

	news = News.objects.all()
	sections = Section.objects.all()
	subsections = Section.objects.all()
	 

	return render(request, 'newspaper/userAuthenticated/manager.html', locals())