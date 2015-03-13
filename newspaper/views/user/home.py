from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from newspaper.models import Section

def home(request):
	sections = []
	try:
		sections = Section.objects.all()
		print len(sections)
	except:
		print "Erro ao pegar as paginas"
		pass
	return render(request, 'newspaper/user/home.html', locals())