from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth.views import logout as logout_sys
from newspaper.forms import PartialLectorForm
from newspaper.models import Lector
from django.utils.translation import ugettext as _
from .home import home
from newspaper.entities import Message, TypeMessage,TextMessage

try:
	from hashlib import md5
except:
	from md5 import new as md5

def login(request):
	message = None
	if request.user.is_authenticated():
		return HttpResponseRedirect("/newspaper/")
	
	if request.method == "POST":
		try:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
		except:
			message = Message(TextMessage.ERROR_GET_PARAMETERS, TypeMessage.ERROR)
			return home(request,None, None, message)

		if user:
			login_user(request, user)
			if request.user.is_authenticated():
				message = Message(TextMessage.LOGIN_SUCCESS, TypeMessage.SUCCESS)
			else:
				message = Message(TextMessage.LOGIN_ERROR, TypeMessage.ERROR)
		else:
			message = Message(TextMessage.LOGIN_ERROR, TypeMessage.ERROR)
	else:
		message = Message(TextMessage.POST_REQUIRED, TypeMessage.ERROR)
	return home(request,None, None, message)

def logout(request):
	message = None
	logout_sys(request)
	messages = Message(TextMessage.LOGOUT_SUCCESS, TypeMessage.SUCCESS)
	return home(request,None, None, messages)

def signup(request):
	message = None
	if request.method == "POST":
		request.POST = request.POST.copy()
		try:
			request.POST['password'] =  md5(request.POST['password'] ).hexdigest()
		except:
			message = Message(TextMessage.ERROR_GET_PARAMETERS, TypeMessage.ERROR)
			return home(request,None, None, message)

		form = PartialLectorForm(request.POST)
		lector = Lector()
		if lector.registeringLector(form):
			messages = Message(TextMessage.USER_CREATED_SUCCESS, TypeMessage.SUCCESS)
		else:
			messages = Message(TextMessage.USER_CREATED_ERROR, TypeMessage.ERROR)
	else:
		message = Message(TextMessage.POST_REQUIRED, TypeMessage.ERROR)
	return home(request,None, None, messages)

