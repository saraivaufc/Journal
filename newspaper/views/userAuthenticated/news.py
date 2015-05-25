# -*- endcoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _
from newspaper.models import News, Journalist, Redator, Section
from newspaper.forms import NewsForm, PartialNewsForm
from newspaper.entities import Message, TypeMessage, TextMessage
from django.utils.translation import ugettext as _
from newspaper.views.userAuthenticated import manager
from django.contrib.auth.decorators import permission_required


@permission_required('newspaper.keep_news')
def addNews(request):
	message = None
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
		news = News.objects.all()
		sections = Section.objects.all()
		redators = Redator.objects.all()
		journalists = Journalist.objects.all()
		return render(request, "newspaper/userAuthenticated/news/addNews.html", locals())
	return manager(request, None, None,1, message )


@permission_required('newspaper.keep_news')
def editNews(request, id_news):
	message = None
	try:
		news = News.objects.get(id = id_news)
	except:
		message = Message(TextMessage.NEWS_NOT_FOUND, TypeMessage.ERROR)
		return manager(request, None, None,1, message )

	if request.method == "POST":
		try:
			try:
				user = Journalist.objects.get(username=request.user.username)
			except:
				message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
				return manager(request, None, None,1, message )
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
			news = News.objects.all()
			sections = Section.objects.all()
			redators = Redator.objects.all()
			journalists = Journalist.objects.all()
			return render(request, "newspaper/userAuthenticated/news/editNews.html", locals())
		except:
			pass
	return manager(request, None, None,1, message )

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
					return manager(request, None, None,1, message )

			if user.deleteNews(id_news):
				message = Message(TextMessage.NEWS_SUCCESS_REM, TypeMessage.SUCCESS)
			else:
				message = Message(TextMessage.NEWS_ERROR_REM, TypeMessage.ERROR)
		except:
			message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)
	else:
		message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
	return manager(request, None, None,1,  message )