# -*- endcoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _
from newspaper.models import News, Journalist, Redator
from newspaper.forms import NewsForm, PartialNewsForm
from newspaper.entities import Message, TypeMessage, TextMessage
from django.utils.translation import ugettext as _
from newspaper.views.userAuthenticated import manager


def addNews(request):
	message = None
	if request.user.has_perm('newspaper.keep_news'):
		if request.method == "POST":
			try:
				user = Journalist.objects.get(
										username=request.user.username)
				form = PartialNewsForm(request.POST, request.FILES)
				if user.registeringNews(form):
					message = Message(TextMessage.NEWS_SUCCESS_ADD, TypeMessage.SUCCESS)
				else:
					message = Message(TextMessage.NEWS_ERROR_ADD, TypeMessage.ERROR)
			except:
				message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
		else:
			form = PartialNewsForm()
			option = _("News")
			return render(request, "newspaper/userAuthenticated/news/addNews.html", locals())
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)

	return manager(request, None, None, message )

def editNews(request, id_news):
	message = None
	if request.user.has_perm('newspaper.keep_news'):
		try:
			news = News.objects.get(id = id_news)
		except:
			message = Message(TextMessage.NEWS_NOT_FOUND, TypeMessage.ERROR)
			return manager(request, None, None, message )

		if request.method == "POST":
			try:
				try:
					user = Journalist.objects.get(username=request.user.username)
				except:
					message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
					return manager(request, None, None, message )
				form = PartialNewsForm(request.POST, request.FILES, instance=news)
				if user.editNews(form):
					message = Message(TextMessage.NEWS_SUCCESS_EDIT, TypeMessage.SUCCESS)
				else:
					message = Message(TextMessage.NEWS_ERROR_EDIT, TypeMessage.ERROR)
			except:
				message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)

		else:
			try:
				form = PartialNewsForm(instance = news)
				option = _("News")
				return render(request, "newspaper/userAuthenticated/news/editNews.html", locals())
			except:
				pass
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return manager(request, None, None, message )


def remNews(request, id_news):
	message = None
	if request.user.has_perm('newspaper.keep_news') or request.user.has_perm('newspaper.delete_news'):
		try:
			try:
				user = Journalist.objects.get(username=request.user.username)
			except:
				try:
					user = Redator.objects.get(username=request.user.username)
				except:
					message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
					return manager(request, None, None, message )

			if user.deleteNews(id_news):
				message = Message(TextMessage.NEWS_SUCCESS_REM, TypeMessage.SUCCESS)
			else:
				message = Message(TextMessage.NEWS_ERROR_REM, TypeMessage.ERROR)
		except:
			message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return manager(request, None, None, message )