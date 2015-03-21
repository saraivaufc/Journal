#-*- encoding=utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from newspaper.models import Section, News, Classifield, Comment, Lector
from datetime import datetime
from newspaper.utils import getSections, getNewsFromSection
from newspaper.forms import CommentForm, PartialCommentForm
from django.utils.translation import ugettext as _
from newspaper.entities import Message, TypeMessage
from django.utils.translation import ugettext as _
from newspaper.views.user import home

def viewNews(request, id_news):
	news = None
	try:
		news = News.objects.get(id = id_news)
	except:
		message = Message(_("News not found!!!"), TypeMessage.ERROR)

	if request.method == 'POST':
		if request.user.is_authenticated():			
			if request.user.has_perm('newspaper.comment_news'):
				try:
					try:
						lector = Lector.objects.get(username = request.user.username)
					except:
						message = Message(_("User does not exist!!!"), TypeMessage.ERROR)
					try:
						image = request.FILES['image']
					except:
						image = ''
					if lector.commentNews(news, lector, request.POST['text'], image):
						message = Message(_("Comment successfully added!!!"), TypeMessage.SUCCESS)
					else:
						message = Message(_("Error adding comment!!!"), TypeMessage.ERROR)
				except:
					message = Message(_("Unable to comment on the news!!!"), TypeMessage.ERROR)
			else:
				message = Message(_("User does not have permission!!!"), TypeMessage.INFO)
		else:
			message = Message(_("User is not authenticated!!!"), TypeMessage.INFO)

	sections = []
	sections = Section.objects.filter()
	try:
		sections = Section.objects.all()
		sec  = getSections(news)
		news_all = []
		for i in sec:
			for k in getNewsFromSection(i):
				if k.id != news.id:
					news_all.append(k)
	except:
		pass
	
	form = PartialCommentForm()
	return render(request, 'newspaper/user/news.html', locals())