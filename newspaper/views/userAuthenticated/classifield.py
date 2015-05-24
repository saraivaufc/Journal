# -*- endcoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _
from newspaper.utils import filterList
from newspaper.models import Redator, Classifield, News, Journalist, Section, SubSection, Offer
from newspaper.forms import ClassifieldForm, PartialClassifieldForm
from newspaper.entities import Message, TypeMessage,TextMessage
from django.utils.translation import ugettext as _
from newspaper.views.userAuthenticated import manager
from django.contrib.auth.decorators import permission_required

@permission_required('newspaper.keep_classifield')
def viewClassifield(request, id_page = 1, message = None):
	try:
		id_page = int(id_page)
	except:
		id_page = 1
	open_classfield = True
	try:
		classifields = Classifield.objects.all()
		classifields = filterList(classifields, int(id_page), 10)
		id_page_left = int(id_page) - 1
		if id_page_left <= 0: id_page_left = 1
		id_page_rigth = int(id_page) + 1
		if len(filterList(classifields, int(id_page_rigth), 10)) == 0: id_page_rigth = None
		news = News.objects.all()
		sections = Section.objects.all()
		journalists = Journalist.objects.all()
		redators = Redator.objects.all()
		return render(request, "newspaper/userAuthenticated/classifield/viewClassifields.html", locals())
	except:
		message = Message(TextMessage.CLASSIFIELDS_NOT_FOUND, TypeMessage.ERROR)
	return viewClassifield(request,id_page, message )


@permission_required('newspaper.keep_classifield')
def addClassifield(request):
	message = None
	open_classfield = True
	if request.method == "POST":
		try:
			try:
				user = Redator.objects.get(username=request.user.username)
			except:
				message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
				return manager(request, None, None,1,  message )
			form = PartialClassifieldForm(request.POST, request.FILES)
			if user.registeringClassifield(form):
				message = Message(TextMessage.CLASSIFIELD_SUCCESS_ADD, TypeMessage.SUCCESS)
			else:
				message = Message(TextMessage.CLASSIFIELD_ERROR_ADD, TypeMessage.ERROR)
		except:
			pass
		return viewClassifield(request, 1, message )
	else:
		form = PartialClassifieldForm()
		option = _("Classifield")

		news = News.objects.all()
		sections = Section.objects.all()
		journalists = Journalist.objects.all()
		redators = Redator.objects.all()
		return render(request, "newspaper/userAuthenticated/classifield/addClassifield.html", locals())
	return viewClassifield(request,1,message )


@permission_required('newspaper.keep_classifield')
def remClassifield(request, id_classifield):
	message = None
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
	return viewClassifield(request,1, message)

@permission_required('newspaper.keep_classifield')
def editClassifield(request, id_classifield):
	message = None
	open_classfield = True
	try:
		classifield = Classifield.objects.get(id = id_classifield)
	except:
		message = Message(TextMessage.CLASSIFIELD_NOT_FOUND, TypeMessage.ERROR)
		return manager(request, None, None, 1, message )
	if request.method == "POST":
		try:
			user = Redator.objects.get(username = request.user.username)
		except:
			message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
			return manager(request, None, None, 1, message )
		form = PartialClassifieldForm(request.POST, request.FILES, instance = classifield)
		if user.editClassifield(form):
			message = Message(TextMessage.CLASSIFIELD_SUCCESS_EDIT, TypeMessage.SUCCESS)
		else:
			message = Message(TextMessage.CLASSIFIELD_ERROR_EDIT, TypeMessage.ERROR)
	else:
		form = PartialClassifieldForm(instance = classifield) 
		news = News.objects.all()
		sections = Section.objects.all()
		journalists = Journalist.objects.all()
		redators = Redator.objects.all()
		return render(request, "newspaper/userAuthenticated/classifield/editClassifield.html", locals())
	return viewClassifield(request,1, message)