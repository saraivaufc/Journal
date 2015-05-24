# -*- endcoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _
from newspaper.models import News, Redator,Section, SubSection
from newspaper.forms import RedatorForm, PartialRedatorForm
from newspaper.entities import Message, TypeMessage,TextMessage
from django.utils.translation import ugettext as _
from newspaper.views.userAuthenticated import manager
try:
	from hashlib import md5
except:
	from md5 import new as md5

def addRedator(request):
	message = None
	if request.user.has_perm('newspaper.keep_redator') :
		news = News.objects.all()
		sections = Section.objects.all()
		redators = Redator.objects.all()
		if request.method == "POST":
			try:
				request.POST = request.POST.copy()
				request.POST['password'] =  md5(request.POST['password'] ).hexdigest()
			except:
				pass
			form = PartialRedatorForm(request.POST, request.FILES)
			try:
				user = Redator.objects.get(username = request.user.username)
			except:
				message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.SUCCESS)
				return manager(request, None, None,1, message)
				
			if user.registeringRedator(form):
				message = Message(TextMessage.REDATOR_SUCCESS_ADD, TypeMessage.SUCCESS)
			else:
				message = Message(TextMessage.REDATOR_ERROR_ADD, TypeMessage.ERROR)

			return manager(request, None, None,1, message )
		form = PartialRedatorForm()
		option = _("Redator")
		open_redator = True
		return render(request, "newspaper/userAuthenticated/redator/addRedator.html", locals())
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return manager(request, None, None,1, message )

def viewRedator(request, id_redator):
	message = None
	if request.user.has_perm('newspaper.keep_redator'):
		news = News.objects.all()
		sections = Section.objects.all()
		try:
			try:
				redator = Redator.objects.get(id = id_redator)
			except:
				message = Message(TextMessage.REDATOR_NOT_FOUND, TypeMessage.ERROR)
			redators = Redator.objects.all()
			open_redator = True
			return render(request, "newspaper/userAuthenticated/redator/viewRedator.html", locals())
		except:
			message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return manager(request, None, None,1, message )

def remRedator(request, id_redator):
	message = None
	if request.user.has_perm('newspaper.keep_redator'):
		try:
			user = Redator.objects.get(username = request.user.username)
			if user.remRedator(id_redator):
				message = Message(TextMessage.REDATOR_SUCCESS_REM, TypeMessage.SUCCESS)
			else:
				message = Message(TextMessage.REDATOR_ERROR_REM, TypeMessage.ERROR)
		except:
			message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return manager(request, None, None, 1, message )

def editRedator(request, id_redator):
	message = None
	if request.user.has_perm('newspaper.keep_redator'):
		news = News.objects.all()
		sections = Section.objects.all()
		try:
			try:
				user = Redator.objects.get(username = request.user.username)
			except:
				message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)

			try:
				redator = Redator.objects.get(id = id_redator)
			except:
				message = Message(TextMessage.REDATOR_ERROR_REM, TypeMessage.ERROR)
			redators = Redator.objects.all()
		except:
			message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)

		if request.method == "POST":
			form = PartialRedatorForm(request.POST, request.FILES, instance = redator)
			if user.editRedator(form):
				message = Message(TextMessage.REDATOR_SUCCESS_EDIT, TypeMessage.SUCCESS)
			else:
				message = Message(TextMessage.REDATOR_ERROR_EDIT, TypeMessage.ERROR)
		else:
			form = PartialRedatorForm(instance = redator) 
			open_redator = True
			return render(request, "newspaper/userAuthenticated/redator/editRedator.html", locals())
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return manager(request, None, None, 1, message )