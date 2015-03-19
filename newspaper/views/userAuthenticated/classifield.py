# -*- endcoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _
from newspaper.models import Redator, Classifield, News, Journalist, Section, SubSection
from newspaper.forms import ClassifieldForm, PartialClassifieldForm

def addClassifield(request):
	open_classfield = True
	if request.user.has_perm('newspaper.keep_classifield'):
		news = News.objects.all()
		sections = Section.objects.all()
		if request.user.has_perm('newspaper.keep_journalist'):
			journalists = Journalist.objects.all()

		if request.method == "POST":
			try:
				user = Redator.objects.get(
										username=request.user.username)
				form = PartialClassifieldForm(request.POST, request.FILES)
				user.registeringClassifield(form)
			except:
				pass
			return HttpResponseRedirect("/newspaper/userAuthenticated/manager/classifield/view/")
		else:
			form = PartialClassifieldForm()
			option = _("Classifield")
			return render(request, "newspaper/userAuthenticated/classifield/addClassifield.html", locals())
	else:
		print "Sem permisão"
	return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")

def viewClassifield(request):
	open_classfield = True
	if request.user.has_perm('newspaper.keep_classifield'):
		news = News.objects.all()
		sections = Section.objects.all()
		if request.user.has_perm('newspaper.keep_journalist'):
			journalists = Journalist.objects.all()
		try:
			classifields = Classifield.objects.all()
			return render(request, "newspaper/userAuthenticated/classifield/viewClassifields.html", locals())
		except:
			print "Erro ao poasdoakd"
	else:
		print "Sem permisão"
	return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")

def remClassifield(request, id_classifield):
	if request.user.has_perm('newspaper.keep_classifield'):
		try:
			user = Redator.objects.get(username = request.user.username)
			user.remClassifield(id_classifield)
		except:
			print "Erro ao pegar Usuario"
	else:
		print "Sem permisão"
	return HttpResponseRedirect("/newspaper/userAuthenticated/manager/classifield/view/")

def editClassifield(request, id_classifield):
	open_classfield = True
	if request.user.has_perm('newspaper.keep_classifield'):
		news = News.objects.all()
		sections = Section.objects.all()
		if request.user.has_perm('newspaper.keep_journalist'):
			journalists = Journalist.objects.all()
		try:
			user = Redator.objects.get(username = request.user.username)
			classifield = Classifield.objects.get(id = id_classifield)
		except:
			print "Erro ao pegar Usuario ou jornalista"
			return HttpResponseRedirect("/newspaper/userAuthenticated/manager/classifield/view/")

		if request.method == "POST":
			form = PartialClassifieldForm(request.POST, request.FILES, instance = classifield)
			user.editJournalist(form)
		else:
			form = PartialClassifieldForm(instance = classifield) 
			return render(request, "newspaper/userAuthenticated/classifield/editClassifield.html", locals())
	else:
		print "Sem permisão"
	return HttpResponseRedirect("/newspaper/userAuthenticated/manager/classifield/view/")