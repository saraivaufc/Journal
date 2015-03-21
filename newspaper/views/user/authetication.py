from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth.views import logout as logout_sys
from newspaper.forms import PartialLectorForm
from newspaper.models import Lector
from newspaper.entities import Message, TypeMessage
from django.utils.translation import ugettext as _
from .home import home

try:
	from hashlib import md5
except:
	from md5 import new as md5

def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/newspaper/")
	
	if request.method == "POST":
		try:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
		except:
			messages = Message(_("Detected intrusion attempt!!!"), TypeMessage.ERROR)

		if user:
			login_user(request, user)
			if request.user.is_authenticated():
				messages = Message(_("Login successfully performed!!!"), TypeMessage.SUCCESS)
			else:
				messages = Message(_("Failed to perform login!!!"), TypeMessage.ERROR)
		else:
			messages = Message(_("Failed to perform login!!!"), TypeMessage.ERROR)

	else:
		messages = Message(_("Failed to perform login!!!"), TypeMessage.ERROR)
	return home(request,None, None, messages)

def logout(request):
	logout_sys(request)
	messages = Message(_("Logout successfully performed!!!"), TypeMessage.SUCCESS)
	return home(request,None, None, messages)

def signup(request):
	if request.method == "POST":
		request.POST = request.POST.copy()
		request.POST['password'] =  md5(request.POST['password'] ).hexdigest()
		form = PartialLectorForm(request.POST)
		lector = Lector()
		if lector.registeringLector(form):
			messages = Message(_("User created successfully!!!"), TypeMessage.SUCCESS)
		else:
			messages = Message(_("Failed to create user!!!"), TypeMessage.ERROR)

	return home(request,None, None, messages)

