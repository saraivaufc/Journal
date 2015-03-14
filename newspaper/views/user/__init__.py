# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from newspaper.models import Redator, Lector

from .home import *
from .news import *
from .classifield import *

def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/home/')
	else:
		return HttpResponseRedirect('/userAutheticated/home/')