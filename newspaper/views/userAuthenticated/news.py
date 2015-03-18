# -*- endcoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _
from newspaper.models import News, Journalist
from newspaper.forms import NewsForm, PartialNewsForm

def addNews(request):
	if request.user.has_perm('newspaper.keep_news'):
		if request.method == "POST":
			try:
				user = Journalist.objects.get(
										username=request.user.username)
				form = PartialNewsForm(request.POST, request.FILES)
				user.registeringNews(form)
			except:
				pass
			return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")
		else:
			form = PartialNewsForm
			option = _("News")
			return render(request, "newspaper/userAuthenticated/news/addNews.html", locals())
	else:
		print "Sem permisão"
	return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")

def editNews(request, id_news):
	if request.user.has_perm('newspaper.keep_news'):
		try:
			news = News.objects.get(id = id_news)
		except:
			return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")

		if request.method == "POST":
			user = Journalist.objects.get(
										username=request.user.username)
			form = PartialNewsForm(request.POST, request.FILES, instance=news)
			user.editNews(form)
		else:
			try:
				form = PartialNewsForm(instance = news)
				option = _("News")
				return render(request, "newspaper/userAuthenticated/news/editNews.html", locals())
			except:
				pass
	else:
		print "Sem Permissão"
	return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")


def remNews(request, id_news):
	if request.user.has_perm('newspaper.keep_news') or request.user.has_perm('newspaper.delete_news'):
		try:
			News.objects.get(id = id_news).delete()
		except Exception, e:
			raise e
	return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")