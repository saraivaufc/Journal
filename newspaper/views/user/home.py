from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from newspaper.models import Section, News, Classifield
from datetime import datetime
from newspaper.utils import getNewsFromSection

def home(request, id_section=None, id_subsection=None):
	sections = []
	sections = Section.objects.filter()
	if id_section != None:
		section = Section.objects.get(id = int(id_section))
		news_filter = getNewsFromSection(section)
	else:
		news_filter = News.objects.filter().order_by('-dating_news')
	if id_subsection != None:
		news_all = []
		for i in news_filter:
			print i.subsection_id,id_subsection 
			if i.subsection_id == int(id_subsection):
				news_all.append(i)
	else:
		news_all = news_filter		

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