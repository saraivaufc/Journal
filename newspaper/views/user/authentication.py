from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth.views import logout as logout_sys
from newspaper.forms import PartialLectorForm
from newspaper.models import Lector, Anonymous

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
		except:
			pass

		user = authenticate(username=username, password=password)
		if user:
			login_user(request, user)
			return login(request)
		else:
			pass

	else:
		pass
	return HttpResponseRedirect("/newspaper/")

def logout(request):
	logout_sys(request)
	return HttpResponseRedirect("/newspaper/")

def signup(request):
	if request.method == "POST":
		request.POST = request.POST.copy()
		request.POST['password'] =  md5(request.POST['password'] ).hexdigest()
		form = PartialLectorForm(request.POST)
		anonymous = Anonymous()
		anonymous.registering_lector(form)
	return HttpResponseRedirect("/newspaper/")

