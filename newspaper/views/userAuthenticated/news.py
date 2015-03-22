# -*- endcoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _
from newspaper.models import News, Journalist
from newspaper.forms import NewsForm, PartialNewsForm
from newspaper.entities import Message, TypeMessage
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
					message = Message(_("News added successfully!!!"), TypeMessage.SUCCESS)
				else:
					message = Message(_("Failed to add the news!!!"), TypeMessage.ERROR)
			except:
				message = Message(_("Journalist does not exist!!!"), TypeMessage.ERROR)
		else:
			form = PartialNewsForm()
			option = _("News")
			return render(request, "newspaper/userAuthenticated/news/addNews.html", locals())
	else:
		message = Message(_("User does not have permission!!!"), TypeMessage.ERROR)

	return manager(request, None, None, message )

def editNews(request, id_news):
	message = None
	if request.user.has_perm('newspaper.keep_news'):
		try:
			news = News.objects.get(id = id_news)
		except:
			return HttpResponseRedirect("/newspaper/userAuthenticated/manager/")

		if request.method == "POST":
			try:
				user = Journalist.objects.get(
											username=request.user.username)
				form = PartialNewsForm(request.POST, request.FILES, instance=news)
				if user.editNews(form):
					message = Message(_("News edited successfully!!!"), TypeMessage.SUCCESS)
				else:
					message = Message(_("Failed to edit news!!!"), TypeMessage.ERROR)
			except:
				message = Message(_("Journalist does not exist!!!"), TypeMessage.ERROR)

		else:
			try:
				form = PartialNewsForm(instance = news)
				option = _("News")
				return render(request, "newspaper/userAuthenticated/news/editNews.html", locals())
			except:
				pass
	else:
		message = Message(_("User does not have permission!!!"), TypeMessage.ERROR)
	return manager(request, None, None, message )


def remNews(request, id_news):
	message = None
	if request.user.has_perm('newspaper.keep_news') or request.user.has_perm('newspaper.delete_news'):
		try:
			user = Journalist.objects.get(username=request.user.username)
			if user.deleteNews(id_news):
				message = Message(_("Removed successfully News!!!"), TypeMessage.SUCCESS)
			else:
				message = Message(_("Failed to remove news!!!"), TypeMessage.ERROR)
		except:
			message = Message(_("Journalist does not exist!!!"), TypeMessage.ERROR)
	return manager(request, None, None, message )