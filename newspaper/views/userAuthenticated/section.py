# -*- endcoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _
from newspaper.models import Section, SubSection, Redator, News, Journalist
from newspaper.forms import SectionForm, PartialSectionForm, SubSectionForm, PartialSubSectionForm

def addSection(request):
	if request.user.has_perm('newspaper.keep_section'):
		news = News.objects.all()
		sections = Section.objects.all()
		subsections = SubSection.objects.all()
		if request.user.has_perm('newspaper.keep_journalist'):
			journalists = Journalist.objects.all()
		if request.method == "POST":
			try:
				user = Redator.objects.get(
										username=request.user.username)
				form = PartialSectionForm(request.POST, request.FILES)
				user.registeringSection(form)
			except:
				pass
			return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")
		else:
			form = PartialSectionForm()
			option = _("Section")
			open_sections2 = True
			open_subsections2 = True
			return render(request, "newspaper/userAuthenticated/section/addSection.html", locals())
	else:
		print "Sem permisão"
	return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")

def editSection(request, id_section):
	if request.user.has_perm('newspaper.keep_section'):
		news = News.objects.all()
		sections = Section.objects.all()
		if request.user.has_perm('newspaper.keep_journalist'):
			journalists = Journalist.objects.all()
		try:
			section = Section.objects.get(id = id_section)
		except:
			return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")

		if request.method == "POST":
			try:
				user = Redator.objects.get(username=request.user.username)
				form = PartialSectionForm(request.POST, request.FILES, instance=section)
				user.editSection(form)
			except:
				pass
		else:
			try:
				form = PartialSectionForm(instance = section)
				option = _("Section")
				open_sections2 = True
				open_subsections2 = True
				return render(request, "newspaper/userAuthenticated/section/editSection.html", locals())
			except:
				pass
	else:
		print "Sem Permissão"
	return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")


def remSection(request, id_section):
	if request.user.has_perm('newspaper.keep_section'):
		try:
			user = Redator.objects.get(username=request.user.username)
			user.remSection(id_section)
		except:
			pass
	return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")