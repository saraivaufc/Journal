from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from newspaper.models import Section, News, Classifield
from datetime import datetime

def home(request, id_subsection=None):
	sections = []
	sections = Section.objects.filter()
	if id_subsection != None:
		news_all = News.objects.filter(subsection = id_subsection).order_by('-dating_news')
	else:
		news_all = News.objects.filter().order_by('-dating_news')
	news_image = []
	news_no_image = []
	most_popular = []
	classifields = Classifield.objects.all()
	for i in news_all:
		if i.image == '':
			news_no_image.append(i)
		else:
			news_image.append(i)
			most_popular.append(i)
	return render(request, 'newspaper/user/home.html', locals())