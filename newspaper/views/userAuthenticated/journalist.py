# -*- endcoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _
from newspaper.models import News, Redator
from newspaper.forms import JournalistForm, PartialJournalistForm
try:
	from hashlib import md5
except:
	from md5 import new as md5

def remJournalist(request, id_journalist):
	if request.user.has_perm('newspaper.keepjournalist'):
		try:
			Journalist.objects.get(id = id_news).delete()
		except:
			print 'Error'
	return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")

def addJournalist(request):
	if request.user.has_perm('newspaper.keep_journalist') :
		if request.method == "POST":
			try:
				request.POST = request.POST.copy()
				request.POST['password'] =  md5(request.POST['password'] ).hexdigest()
			except:
				print "Erro ao criar hash da senha"
			form = PartialJournalistForm(request.POST, request.FILES)
			try:
				user = Redator.objects.get(username = request.user.username)
			except:
				print "Erro ao pegar Usuario"
			if user.registeringJournalist(form):
				print "Journalist inserido"
			else:
				print "Form Invalid"
			return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")
		form = PartialJournalistForm
		option = _("Journalist")
		return render(request, "newspaper/userAuthenticated/news/addNews.html", locals())
	else:
		return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")