from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from newspaper.models import Section, SubSection, News, Classifield
from datetime import datetime
from newspaper.utils import getNewsFromSection
from newspaper.entities import Message, TypeMessage, TextMessage
from django.utils.translation import ugettext as _

def home(request, id_section=None, id_subsection=None, message = None): 
	sections = []
	sections = Section.objects.filter()
	if id_section != None:
		try:
			section = Section.objects.get(id = int(id_section))
			news_filter = getNewsFromSection(section)
		except:
			news_filter = []
			message = Message(TextMessage.SECTION_NOT_FOUND, TypeMessage.ERROR)
	else:
		news_filter = News.objects.filter().order_by('-dating_news')
	if id_subsection:
		try:
			subsection = SubSection.objects.get(id = id_subsection)
		except:
			message = Message(TextMessage.SUBSECTION_NOT_FOUND, TypeMessage.ERROR)
	if id_subsection != None:
		news_all = []
		for i in news_filter:
			if i.subsection_id == subsection.id:
				news_all.append(i)
	else:
		news_all = news_filter		

	news_image = []
	news_no_image = []
	classifields = Classifield.objects.all()
	for i in news_all:
		if i.image == '':
			news_no_image.append(i)
		else:
			news_image.append(i)
	most_popular = news_image[:5]
	return render(request, 'newspaper/user/home.html', locals())