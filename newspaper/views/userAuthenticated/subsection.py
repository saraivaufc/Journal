# -*- endcoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _
from newspaper.models import Section, SubSection, Redator, News, Journalist
from newspaper.forms import SubSectionForm, PartialSubSectionForm
from newspaper.entities import Message, TypeMessage,TextMessage
from django.utils.translation import ugettext as _
from newspaper.views.userAuthenticated import manager

def addSubSection(request):
	message = None
	if request.user.has_perm('newspaper.keep_subsection'):
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
				form = PartialSubSectionForm(request.POST, request.FILES)
				if user.registeringSubSection(form):
					message = Message(TextMessage.SUBSECTION_SUCCESS_ADD, TypeMessage.SUCCESS)
				else:
					message = Message(TextMessage.SUBSECTION_ERROR_ADD, TypeMessage.ERROR)
			except:
				pass
		else:
			form = PartialSubSectionForm()
			option = _("SubSection")
			open_sections2 = True
			open_subsections2 = True
			return render(request, "newspaper/userAuthenticated/subsection/addSubSection.html", locals())
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return manager(request, None, None, message )

def editSubSection(request, id_subsection):
	message = None
	if request.user.has_perm('newspaper.keep_subsection'):
		news = News.objects.all()
		sections = Section.objects.all()
		if request.user.has_perm('newspaper.keep_journalist'):
			journalists = Journalist.objects.all()
		try:
			subsection = SubSection.objects.get(id = id_subsection)
		except:
			message = Message(TextMessage.SUBSECTION_NOT_FOUND, TypeMessage.ERROR)
			return manager(request, None, None, message )

		if request.method == "POST":
			try:
				try:
					user = Redator.objects.get(username=request.user.username)
				except:
					message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
					return manager(request, None, None, message)
				form = PartialSubSectionForm(request.POST, request.FILES, instance=subsection)
				if user.editSubSection(form):
					message = Message(TextMessage.SUBSECTION_SUCCESS_EDIT, TypeMessage.SUCCESS)
				else:
					message = Message(TextMessage.SUBSECTION_ERROR_EDIT, TypeMessage.ERROR)
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
				message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return manager(request, None, None, message )


def remSubSection(request, id_subsection):
	message = None
	if request.user.has_perm('newspaper.keep_subsection'):
		try:
			try:
				user = Redator.objects.get(username=request.user.username)
			except:
				message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
				return manager(request, None, None, message)
			if user.remSubSection(id_subsection):
				message = Message(TextMessage.SUBSECTION_SUCCESS_REM, TypeMessage.SUCCESS)
			else:
				message = Message(TextMessage.SUBSECTION_ERROR_REM, TypeMessage.ERROR)
		except:
			pass
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return manager(request, None, None, message )