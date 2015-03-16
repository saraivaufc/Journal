#-*- encoding=utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from newspaper.models import Section, News, Classifield, Comment, Lector
from datetime import datetime
from newspaper.utils import getSections, getNewsFromSection
from newspaper.forms import CommentForm, PartialCommentForm
from django.utils.translation import ugettext as _

def viewNews(request, id_news):
	news = None
	try:
		news = News.objects.get(id = id_news)
	except:
		return HttpResponse("Fail")

	if request.method == 'POST':
		print request.FILES
		if request.user.is_authenticated():			
			if request.user.has_perm('newspaper.comment_news'):
				try:
					try:
						lector = Lector.objects.get(username = request.user.username)
					except:
						pass
					try:
						image = request.FILES['image']
					except:
						image = ''
					if lector.commentNews(news, lector, request.POST['text'], image):
						print _("Comment successfully added")
					else:
						print _("Error adding comment")
				except:
					print _("Unable to comment on the news")
			else:
				print _("User does not have permission")
		else:
			print _("User is not authenticated")

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