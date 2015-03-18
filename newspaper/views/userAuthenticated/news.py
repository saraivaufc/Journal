# -*- endcoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _
from newspaper.models import News, Journalist
from newspaper.forms import NewsForm, PartialNewsForm

def remNews(request, id_news):
	if request.user.has_perm('newspaper.keepnews') or request.user.has_perm('newspaper.delete_news'):
		try:
			News.objects.get(id = id_news).delete()
		except Exception, e:
			raise e
	return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")

def addNews(request):
	if request.user.has_perm('newspaper.keep_news'):
		if request.method == "POST":
			user = Journalist.objects.get(
										username=request.user.username)
			form = PartialNewsForm(request.POST, request.FILES)
			user.registeringNews(form)
			return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")
		else:
			form = PartialNewsForm
			option = _("News")
			return render(request, "newspaper/userAuthenticated/news/addNews.html", locals())
	return HttpResponseRedirect("/newspaper/UserAuthenticated/manager/")