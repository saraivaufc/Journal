#-*- encoding=utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from newspaper.models import Section, News, Classifield, Comment, Lector
from datetime import datetime
from newspaper.utils import getSections, getNewsFromSection
from newspaper.forms import CommentForm, PartialCommentForm
from django.utils.translation import ugettext as _
from newspaper.entities import Message, TypeMessage,TextMessage
from django.utils.translation import ugettext as _
from newspaper.views.user import home
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect

@cache_page(60 * 15)
@csrf_protect
def viewNews(request, id_news):
	message = None
	news = None
	try:
		news = News.objects.get(id = id_news)
	except:
		message = Message(TextMessage.NEWS_NOT_FOUND, TypeMessage.ERROR)

	if request.method == 'POST':
		if request.user.is_authenticated():			
			if request.user.has_perm('newspaper.comment_news'):
				try:
					try:
						lector = Lector.objects.get(username = request.user.username)
					except:
						message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
					try:
						image = request.FILES['image']
					except:
						image = ''
					if lector.commentNews(news, lector, request.POST['text'], image):
						message = Message(TextMessage.COMMENT_SUCCESS_ADD, TypeMessage.SUCCESS)
					else:
						message = Message(TextMessage.COMMENT_ERROR_ADD, TypeMessage.ERROR)
				except:
					message = Message(TextMessage.COMMENT_NOT_PERMISSION, TypeMessage.ERROR)
			else:
				message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.INFO)
		else:
			message = Message(TextMessage.USER_NOT_AUTHENTICATED, TypeMessage.INFO)

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