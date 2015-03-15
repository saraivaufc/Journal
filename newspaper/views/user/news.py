from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from newspaper.models import Section, News, Classifield
from datetime import datetime
from newspaper.utils import getSections, getNewsFromSection
def viewNews(request, id_news):
	sections = []
	sections = Section.objects.filter()
	news = None
	#try:
	news = News.objects.get(id = id_news)
	sections = Section.objects.all()
	sec  = getSections(news)
	news_all = []
	for i in sec:
		for k in getNewsFromSection(i):
			if k.id != news.id:
				news_all.append(k)
	#except:
		#print "Erro"
		#pass
	return render(request, 'newspaper/user/news.html', locals())