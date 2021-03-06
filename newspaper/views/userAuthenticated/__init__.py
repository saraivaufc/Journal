# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .manager import *
from .news import *
from .journalist import *
from .redator import *
from .section import *
from .subsection import *
from .classifield import *

def index(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/home/')
	else:
		return HttpResponseRedirect('/userAutheticated/')