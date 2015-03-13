# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from newspaper.models import Redator, Lector

from .user.home import *

def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/newspaper/home/')
	else:
		return HttpResponseRedirect('/newspaper/userAutheticated/home/')


