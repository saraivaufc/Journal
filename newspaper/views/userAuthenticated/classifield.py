# -*- endcoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _
from newspaper.models import Redator, Classifield, News, Journalist, Section, SubSection, Offer
from newspaper.forms import ClassifieldForm, PartialClassifieldForm
from newspaper.entities import Message, TypeMessage,TextMessage
from django.utils.translation import ugettext as _
from newspaper.views.userAuthenticated import manager

def addClassifield(request):
	message = None
	open_classfield = True
	if request.user.has_perm('newspaper.keep_classifield'):
		news = News.objects.all()
		sections = Section.objects.all()
		if request.user.has_perm('newspaper.keep_journalist'):
			journalists = Journalist.objects.all()

		if request.method == "POST":
			try:
				try:
					user = Redator.objects.get(username=request.user.username)
				except:
					message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
					return manager(request, None, None, message )
				form = PartialClassifieldForm(request.POST, request.FILES)
				if user.registeringClassifield(form):
					message = Message(TextMessage.CLASSIFIELD_SUCCESS_ADD, TypeMessage.SUCCESS)
				else:
					message = Message(TextMessage.CLASSIFIELD_ERROR_ADD, TypeMessage.ERROR)
			except:
				pass
			return viewClassifield(request, message )
		else:
			form = PartialClassifieldForm()
			option = _("Classifield")
			return render(request, "newspaper/userAuthenticated/classifield/addClassifield.html", locals())
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return viewClassifield(request, message )

def viewClassifield(request, message = None):
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
			message = Message(TextMessage.CLASSIFIELDS_NOT_FOUND, TypeMessage.ERROR)
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return viewClassifield(request, message )

def remClassifield(request, id_classifield):
	message = None
	if request.user.has_perm('newspaper.keep_classifield'):
		try:
			try:
				user = Redator.objects.get(username = request.user.username)
			except:
				message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
				return viewClassifield(request, message )
			if user.remClassifield(id_classifield):
				message = Message(TextMessage.CLASSIFIELD_SUCCESS_REM, TypeMessage.SUCCESS)
			else:
				message = Message(TextMessage.CLASSIFIELD_ERROR_REM, TypeMessage.ERROR)
		except:
			pass
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return viewClassifield(request, message )

def editClassifield(request, id_classifield):
	message = None
	open_classfield = True
	if request.user.has_perm('newspaper.keep_classifield'):
		news = News.objects.all()
		sections = Section.objects.all()
		if request.user.has_perm('newspaper.keep_journalist'):
			journalists = Journalist.objects.all()
			try:
				classifield = Classifield.objects.get(id = id_classifield)
			except:
				message = Message(TextMessage.CLASSIFIELD_NOT_FOUND, TypeMessage.ERROR)
				return manager(request, None, None, message )
		if request.method == "POST":
			try:
				user = Redator.objects.get(username = request.user.username)
			except:
				message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
				return manager(request, None, None, message )
			form = PartialClassifieldForm(request.POST, request.FILES, instance = classifield)
			if user.editClassifield(form):
				message = Message(TextMessage.CLASSIFIELD_SUCCESS_EDIT, TypeMessage.SUCCESS)
			else:
				message = Message(TextMessage.CLASSIFIELD_ERROR_EDIT, TypeMessage.ERROR)
		else:
			form = PartialClassifieldForm(instance = classifield) 
			return render(request, "newspaper/userAuthenticated/classifield/editClassifield.html", locals())
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return viewClassifield(request, message)