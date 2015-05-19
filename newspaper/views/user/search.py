#-*-  encoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from newspaper.entities import Message, TypeMessage, TextMessage
from newspaper.models import Section, SubSection, News
from newspaper.views.user import home, viewNews
import string
from django.utils.translation import ugettext_lazy as _


def search(request):
	if request.method == "POST":
		search = request.POST['search']

		#verify if is Section
		sections = Section.objects.filter(title = search)
		if len(sections) > 0:
			section = sections[0]
			return home(request, section.id)
		#verify if is SubSection
		subsections = SubSection.objects.filter(title = search)
		if len(subsections) > 0:
			subsection = subsections[0]
			return home(request,None, subsection.id)


		#verify if is News
		news = News.objects.filter(title = search)
		if len(news) > 0:
			news = news[0]
			return viewNews(request, news.id)

		search = filterString(search)
		news = News.objects.all()
		itemsCount = {}
		for i in news:
			itemsCount[i.id] = searchWeight(i.description, search)
		maxItemCount = max(itemsCount.values())

		print itemsCount
		if maxItemCount == 0:
			message = Message(TextMessage.NO_RESULTS_FOUND, TypeMessage.ERROR)
			return home(request, None, None, message)
		try:
			id = None
			for key, value in itemsCount.items():
				if value == maxItemCount:
					id = key

			news = News.objects.get(id = id)
			searchResult = search
			return viewNews(request, news.id)

		except:
			return HttpResponseRedirect('/newspaper/')

	else:
		return HttpResponseRedirect('/newspaper/')


def filterString(text):
	text = text.upper()
	textFilter = text.split(" ")
	textFilter = minimizeStringList(textFilter, 3)
	textFilter = excludePronoums(textFilter)
	textFilter = concatStringList(textFilter)
	return textFilter

def searchWeight(text, phrase):
	text = text.upper()
	phrase = phrase.upper()
	return myCount(text, phrase)

def myCount(text, phrase):
	strings =  phrase.split(' ')
	strings = minimizeStringList(strings, 3)
	strings = excludePronoums(strings)
	if len(strings) == 0:
		return 0
	elif len(strings) == 1:
		return string.count(text, strings[0]) * len(strings[0])
	else:
		counts = map( lambda x:  string.count(text, x) * len(x), strings)
		return sum(counts)

def minimizeStringList(stringList, min_size):
	return filter(lambda x : len(x) >= min_size , stringList)

def concatStringList(stringList):
	if len(stringList) == 0:
		return ""
	elif len(stringList) == 1:
		return stringList[0]
	else:
		return  reduce(lambda x, y : x + " " + y, stringList)


def excludePronoums(stringList):
	dic =['PARA', 'COMO','NAO', "SIM"]

	return filter(lambda x :  len( filter(lambda y :  x == y,  dic )  ) == 0  , stringList)