from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from newspaper.models import Classifield, Section, Lector
from newspaper.forms import PartialOfferForm

def viewClassifield(request, id_classifield):
	try:
		sections = Section.objects.all()
		classifield = Classifield.objects.get(id = id_classifield)
		classifields = Classifield.objects.all().exclude(id = id_classifield)
	except:
		pass
	if request.method == "POST":
		form = PartialOfferForm(request.POST)
		try:
			user = Lector.objects.get(username = request.user.username)
			user.addOffer(id_classifield, form)
		except:
			print "Falha pegar user"


	form = PartialOfferForm()
	return render(request, 'newspaper/user/classifield.html', locals())