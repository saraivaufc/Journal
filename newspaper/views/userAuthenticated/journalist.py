# -*- endcoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _
from newspaper.models import News, Redator, Journalist,Section, SubSection
from newspaper.forms import JournalistForm, PartialJournalistForm
from newspaper.entities import Message, TypeMessage,TextMessage
from django.utils.translation import ugettext as _
from newspaper.views.userAuthenticated import manager
try:
	from hashlib import md5
except:
	from md5 import new as md5

def addJournalist(request):
	message = None
	if request.user.has_perm('newspaper.keep_journalist') :
		news = News.objects.all()
		sections = Section.objects.all()
		journalists = Journalist.objects.all()
		if request.method == "POST":
			try:
				request.POST = request.POST.copy()
				request.POST['password'] =  md5(request.POST['password'] ).hexdigest()
			except:
				pass
			form = PartialJournalistForm(request.POST, request.FILES)
			try:
				user = Redator.objects.get(username = request.user.username)
			except:
				message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.SUCCESS)
				return manager(request, None, None, message)
				
			if user.registeringJournalist(form):
				message = Message(TextMessage.JOURNALIST_SUCCESS_ADD, TypeMessage.SUCCESS)
			else:
				message = Message(TextMessage.JOURNALIST_ERROR_ADD, TypeMessage.ERROR)

			return manager(request, None, None, message )
		form = PartialJournalistForm
		option = _("Journalist")
		open_journalist = True
		return render(request, "newspaper/userAuthenticated/journalist/addJournalist.html", locals())
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return manager(request, None, None, message )

def viewJournalist(request, id_journalist):
	message = None
	if request.user.has_perm('newspaper.keep_journalist'):
		news = News.objects.all()
		sections = Section.objects.all()
		try:
			try:
				journalist = Journalist.objects.get(id = id_journalist)
			except:
				message = Message(TextMessage.JOURNALIST_NOT_FOUND, TypeMessage.ERROR)
			journalists = Journalist.objects.all()
			open_journalist = True
			return render(request, "newspaper/userAuthenticated/journalist/viewJournalist.html", locals())
		except:
			message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return manager(request, None, None, message )

def remJournalist(request, id_journalist):
	message = None
	if request.user.has_perm('newspaper.keep_journalist'):
		try:
			user = Redator.objects.get(username = request.user.username)
			if user.remJournalist(id_journalist):
				message = Message(TextMessage.JOURNALIST_SUCCESS_REM, TypeMessage.SUCCESS)
			else:
				message = Message(TextMessage.JOURNALIST_ERROR_REM, TypeMessage.ERROR)
		except:
			message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return manager(request, None, None, message )

def editJournalist(request, id_journalist):
	message = None
	if request.user.has_perm('newspaper.keep_journalist'):
		news = News.objects.all()
		sections = Section.objects.all()
		try:
			try:
				user = Redator.objects.get(username = request.user.username)
			except:
				message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)

			try:
				journalist = Journalist.objects.get(id = id_journalist)
			except:
				message = Message(TextMessage.JOURNALIST_ERROR_REM, TypeMessage.ERROR)
			journalists = Journalist.objects.all()
		except:
			message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)

		if request.method == "POST":
			form = PartialJournalistForm(request.POST, request.FILES, instance = journalist)
			if user.editJournalist(form):
				message = Message(TextMessage.JOURNALIST_SUCCESS_EDIT, TypeMessage.SUCCESS)
			else:
				message = Message(TextMessage.JOURNALIST_ERROR_EDIT, TypeMessage.ERROR)
		else:
			form = PartialJournalistForm(instance = journalist) 
			open_journalist = True
			return render(request, "newspaper/userAuthenticated/journalist/editJournalist.html", locals())
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return manager(request, None, None, message )