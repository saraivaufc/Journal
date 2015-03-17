from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from newspaper.models import Classifield, Section

def viewClassifield(request, id_classifield):
	try:
		sections = Section.objects.all()
		classifield = Classifield.objects.get(id = id_classifield)
		classifields = Classifield.objects.all().exclude(id = id_classifield)
	except:
		pass
	return render(request, 'newspaper/user/classifield.html', locals())