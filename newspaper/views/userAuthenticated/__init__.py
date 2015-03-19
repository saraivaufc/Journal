# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .manager import *
from .news import *
from .journalist import *
from .section import *
from .subsection import *

def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/home/')
	else:
		return HttpResponseRedirect('/userAutheticated/')