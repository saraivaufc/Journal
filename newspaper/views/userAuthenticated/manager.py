# -*- endcoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from newspaper.models import News, Section, SubSection, Journalist
from newspaper.utils import getNewsFromSection
from newspaper.entities import Message, TypeMessage
from django.utils.translation import ugettext as _
from newspaper.views.user import home

def manager(request, id_section = None, id_subsection = None):
	if not request.user.has_perm('newspaper.access_manager'):
		message = Message(_("You do not have access!!!"), TypeMessage.ERROR)
		return home(request,None, None, message)

	news = News.objects.all()
	sections = Section.objects.all()
	if request.user.has_perm('newspaper.keep_journalist'):
		journalists = Journalist.objects.all()

	if id_section == None and id_subsection == None:
		news = News.objects.all()
	elif id_section != None and id_subsection == None:
		try:
			section = Section.objects.get(id = id_section)
			news = getNewsFromSection(section)
			open_sections = True
		except:
			news = []
	elif id_subsection != None:
		try:
			news = News.objects.filter(subsection = id_subsection)
			open_sections = True
			open_subsections = True
		except:
			news = []

	return render(request, 'newspaper/userAuthenticated/manager.html', locals())