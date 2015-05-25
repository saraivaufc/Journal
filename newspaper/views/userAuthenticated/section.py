# -*- endcoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _
from newspaper.models import Section, SubSection, Redator, News, Journalist
from newspaper.forms import SectionForm, PartialSectionForm, SubSectionForm, PartialSubSectionForm
from newspaper.entities import Message, TypeMessage,TextMessage
from django.utils.translation import ugettext as _
from newspaper.views.userAuthenticated import manager

def addSection(request):
	message = None 
	if request.user.has_perm('newspaper.keep_section'):
		if request.method == "POST":
			try:
				try:
					user = Redator.objects.get(username=request.user.username)
				except:
					message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
					return manager(request, None, None,1, message )
				form = PartialSectionForm(request.POST, request.FILES)
				if user.registeringSection(form):
					message = Message(TextMessage.SECTION_SUCCESS_ADD, TypeMessage.SUCCESS)
				else:
					message = Message(TextMessage.SECTION_ERROR_ADD, TypeMessage.ERROR)
			except:
				pass
			return manager(request, None, None,1, message )
		else:
			form = PartialSectionForm()
			option = _("Section")
			open_sections2 = True
			open_subsections2 = True
			

			news = News.objects.all()
			sections = Section.objects.all()
			journalists = Journalist.objects.all()
			redators = Redator.objects.all()
			return render(request, "newspaper/userAuthenticated/section/addSection.html", locals())
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return manager(request, None, None,1,  message )

def editSection(request, id_section):
	message = None
	if request.user.has_perm('newspaper.keep_section'):
		try:
			section = Section.objects.get(id = id_section)
		except:
			message = Message(TextMessage.SECTION_NOT_FOUND, TypeMessage.ERROR)
			return manager(request, None, None,1, message )

		if request.method == "POST":
			try:
				try:
					user = Redator.objects.get(username=request.user.username)
				except:
					message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
					return manager(request, None, None,1, message )

				form = PartialSectionForm(request.POST, request.FILES, instance=section)
				if user.editSection(form):
					message = Message(TextMessage.SECTION_SUCCESS_EDIT, TypeMessage.SUCCESS)
				else:
					message = Message(TextMessage.SECTION_ERROR_EDIT, TypeMessage.ERROR)
			except:
				pass
		else:
			try:
				form = PartialSectionForm(instance = section)
				option = _("Section")
				open_sections2 = True
				open_subsections2 = True
				
				news = News.objects.all()
				sections = Section.objects.all()
				journalists = Journalist.objects.all()
				redators = Redator.objects.all()
				return render(request, "newspaper/userAuthenticated/section/editSection.html", locals())
			except:
				pass
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return manager(request, None, None,1, message )


def remSection(request, id_section):
	message = None
	if request.user.has_perm('newspaper.keep_section'):
		try:
			try:
				user = Redator.objects.get(username=request.user.username)
			except:
				message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
				return manager(request, None, None,1, message )
			if user.remSection(id_section):
				message = Message(TextMessage.SECTION_SUCCESS_REM, TypeMessage.SUCCESS)
			else:
				message = Message(TextMessage.SECTION_ERROR_REM, TypeMessage.ERROR)
		except:
			pass
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return manager(request, None, None,1, message )