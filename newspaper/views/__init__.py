# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/newspaper/home/')
	else:
		return HttpResponseRedirect('/newspaper/userAuthenticated/')


