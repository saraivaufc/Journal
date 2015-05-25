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
from django.contrib.auth.decorators import permission_required


@permission_required('newspaper.keep_journalist')
def viewJournalist(request, id_journalist):
	message = None
	try:
		try:
			journalist = Journalist.objects.get(id = id_journalist)
		except:
			message = Message(TextMessage.JOURNALIST_NOT_FOUND, TypeMessage.ERROR)
		open_journalist = True
		option = _("Journalist")
		news = News.objects.all()
		sections = Section.objects.all()
		journalists = Journalist.objects.all()
		redators = Redator.objects.all()
		return render(request, "newspaper/userAuthenticated/journalist/viewJournalist.html", locals())
	except:
		message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
	return manager(request, None, None,1, message )

@permission_required('newspaper.keep_journalist')
def addJournalist(request):
	message = None
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
			return manager(request, None, None,1, message)
			
		if user.registeringJournalist(form):
			message = Message(TextMessage.JOURNALIST_SUCCESS_ADD, TypeMessage.SUCCESS)
		else:
			message = Message(TextMessage.JOURNALIST_ERROR_ADD, TypeMessage.ERROR)

		return manager(request, None, None,1, message )
	form = PartialJournalistForm()
	option = _("Journalist")
	open_journalist = True

	news = News.objects.all()
	sections = Section.objects.all()
	journalists = Journalist.objects.all()
	redators = Redator.objects.all()
	return render(request, "newspaper/userAuthenticated/journalist/addJournalist.html", locals())


@permission_required('newspaper.keep_journalist')
def remJournalist(request, id_journalist):
	message = None
	try:
		user = Redator.objects.get(username = request.user.username)
		if user.remJournalist(id_journalist):
			message = Message(TextMessage.JOURNALIST_SUCCESS_REM, TypeMessage.SUCCESS)
		else:
			message = Message(TextMessage.JOURNALIST_ERROR_REM, TypeMessage.ERROR)
	except:
		message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
	return manager(request, None, None,1, message )

@permission_required('newspaper.keep_journalist')
def editJournalist(request, id_journalist):
	message = None
	try:
		try:
			user = Redator.objects.get(username = request.user.username)
		except:
			message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)

		try:
			journalist = Journalist.objects.get(id = id_journalist)
		except:
			message = Message(TextMessage.JOURNALIST_ERROR_REM, TypeMessage.ERROR)
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
		option = _("Journalist")
		news = News.objects.all()
		sections = Section.objects.all()
		journalists = Journalist.objects.all()
		redators = Redator.objects.all()
		return render(request, "newspaper/userAuthenticated/journalist/editJournalist.html", locals())
	return manager(request, None, None,1, message )