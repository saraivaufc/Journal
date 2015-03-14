from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from newspaper.models import Section, News, Classifield
from datetime import datetime

def home(request):
	sections = []
	#try:
	sections = Section.objects.all()
	news_all = News.objects.all().order_by('-dating_news')
	news_image = []
	news_no_image = []
	classifields = Classifield.objects.all()
	for i in news_all:
		if i.image == '':
			news_no_image.append(i)
		else:
			news_image.append(i)
	#except:
	#	print "Erro ao pegar as paginas"
	return render(request, 'newspaper/user/home.html', locals())