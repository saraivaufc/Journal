# -*- endcoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _
from newspaper.models import Section, SubSection, Redator, News, Journalist
from newspaper.forms import SubSectionForm, PartialSubSectionForm

def addSubSection(request):
	if request.user.has_perm('newspaper.keep_subsection'):
		news = News.objects.all()
		sections = Section.objects.all()
		if request.user.has_perm('newspaper.keep_journalist'):
			journalists = Journalist.objects.all()
		if request.method == "POST":
			try:
				user = Redator.objects.get(
										username=request.user.username)
				form = PartialSubSectionForm(request.POST, request.FILES)
				user.registeringSubSection(form)
			except:
				pass
			return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")
		else:
			form = PartialSubSectionForm()
			option = _("SubSection")
			open_sections2 = True
			open_subsections2 = True
			return render(request, "newspaper/userAuthenticated/subsection/addSubSection.html", locals())
	else:
		print "Sem permisão"
	return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")

def editSubSection(request, id_subsection):
	if request.user.has_perm('newspaper.keep_subsection'):
		news = News.objects.all()
		sections = Section.objects.all()
		if request.user.has_perm('newspaper.keep_journalist'):
			journalists = Journalist.objects.all()
		try:
			subsection = SubSection.objects.get(id = id_subsection)
		except:
			return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")

		if request.method == "POST":
			try:
				user = Redator.objects.get(username=request.user.username)
				form = PartialSubSectionForm(request.POST, request.FILES, instance=subsection)
				user.editSubSection(form)
			except:
				pass
		else:
			try:
				form = PartialSubSectionForm(instance = subsection)
				option = _("SubSection")
				open_sections2 = True
				open_subsections2 = True
				return render(request, "newspaper/userAuthenticated/subsection/editSubSection.html", locals())
			except:
				pass
	else:
		print "Sem Permissão"
	return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")


def remSubSection(request, id_subsection):
	if request.user.has_perm('newspaper.keep_subsection'):
		try:
			user = Redator.objects.get(username=request.user.username)
			user.remSubSection(id_subsection)
		except:
			pass
	return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")